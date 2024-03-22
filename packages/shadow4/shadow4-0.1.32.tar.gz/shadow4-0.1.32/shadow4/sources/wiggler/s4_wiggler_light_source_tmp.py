"""
Wiggler light source.
"""
#
# Wiggler code: computes wiggler radiation distributions and samples rays according to them.
#
# The radiation is calculating using sr-xraylib
import numpy

from srxraylib.util.inverse_method_sampler import Sampler1D, Sampler2D
from srxraylib.sources.srfunc import wiggler_trajectory, wiggler_spectrum, wiggler_cdf, sync_f

import scipy
from scipy.interpolate import interp1d
from scipy.interpolate import griddata, CloughTocher2DInterpolator, LinearNDInterpolator
import scipy.constants as codata

from shadow4.sources.s4_electron_beam import S4ElectronBeam
from shadow4.sources.s4_light_source import S4LightSource
from shadow4.sources.wiggler.s4_wiggler import S4Wiggler
from shadow4.beam.s4_beam import S4Beam

from shadow4.tools.arrayofvectors import vector_cross, vector_norm

from shadow4.tools.sync_f_sigma_and_pi import sync_f_sigma_and_pi
import time




###############################################

class Sampler1Dcdf(object):

    """
    Constructor.

    Parameters
    ----------
    pdf : numpy array
        1D input probability distrubution function.
    pdf_x : numpy array
        the abscissas of the odf.
    cdf_interpolation_factor : float, optional
        interpolation factor for calculating the cdf (1 makes no interpolation)/

    """
    def __init__(self, cdf, pdf_x=None):

        self._cdf = cdf
        if pdf_x is None:
            self._set_default_pdf_x()
        else:
            self._pdf_x = pdf_x
        self._cdf_x = self._pdf_x.copy()
        self._cdf_interpolation_factor = 1.0

        if self._cdf_x.size != self._cdf_x.size:
            raise Exception("Incompatible arrays.")

    def abscissas(self):
        """
        Gets the abscissas array.

        Returns
        -------
        numpy array
            The abscissas array (referenced, not copied).
        """
        return self._pdf_x

    def cdf(self):
        """
        Gets the cumulative distribution function (cdf).

        Returns
        -------
        numpy array
            The cdf (referenced, not copied).

        """
        return self._cdf

    def cdf_abscissas(self):
        """
        Gets the abscissas of the cumulative distribution function (cdf).

        Returns
        -------
        numpy array
            The cdf abscissas (referenced, not copied).

        """
        return self._cdf_x

    def get_sampled(self, random_in_0_1):
        """
        Return an array with sampled points.

        Parameters
        ----------
        random_in_0_1  : float or numpy array
            Points sampled in a uniform interval.

        Returns
        -------
        numpy array
            the points sampled with the current pdf. The number of points is equal to the dimension of random_in_0_1.

        """
        y = numpy.array(random_in_0_1)

        if y.size > 1:
            x_rand_array = numpy.zeros_like(random_in_0_1)
            for i,cdf_rand in enumerate(random_in_0_1):
                ival,idelta,pendent = self._get_index(cdf_rand)
                x_rand_array[i] = self._pdf_x[ival] + idelta*(self._pdf_x[1]-self._pdf_x[0])
            return x_rand_array
        else:
            ival,idelta,pendent = self._get_index(random_in_0_1)
            return self._pdf_x[int(ival)] + idelta*(self._pdf_x[1]-self._pdf_x[0])

    def get_sampled_and_histogram(self, random_in_0_1, bins=51, range=None):
        """
        Return an array with sampled points and the histogram.

        Parameters
        ----------
        random_in_0_1  : float or numpy array
            Points sampled in a uniform interval.
            bins : int, optional
                Number of bins
            range : list or tuple
                [min, max] the histogram limits.

        Returns
        -------
        tuple
            (s1, h, bin_edges)
            s1: the points sampled with the current pdf. The number of points is equal to the dimension of random_in_0_1,
            h: the array with the histogram values at the bin edges,
            bin_edges: the bin edges.

        """
        s1 = self.get_sampled(random_in_0_1)
        if range is None:
            range = [self._pdf_x.min(),self._pdf_x.max()]
        #
        # histogram
        #
        h, bin_edges = numpy.array(numpy.histogram(s1,bins=bins,range=range))
        return s1, h, bin_edges

    def get_n_sampled_points(self, npoints, seed=None):
        """
        Returns a given number points sampled points sampled with the pdf.

        Parameters
        ----------
        npoints : int
            The number of points.
        seed : int, optional
            The seed (numpy generator is initialized with numpy.random.default_rng(seed))

        Returns
        -------
        numpy array
            The sampled points.

        """
        if not seed is None:
            rng = numpy.random.default_rng(seed)
            cdf_rand_array = rng.random(npoints)
        else:
            cdf_rand_array = numpy.random.random(npoints)

        return self.get_sampled(cdf_rand_array)

    def get_n_sampled_points_and_histogram(self, npoints, bins=51, range=None, seed=None):
        """
        Returns a given number points sampled points sampled with the pdf and the histogram.

        Parameters
        ----------
        npoints : int
            The number of points.
        seed : int, optional
            The seed (numpy generator is initialized with numpy.random.default_rng(seed))
        bins : int, optional
            Number of bins
        range : list or tuple
            [min, max] the histogram limits.

        Returns
        -------
        tuple
            (s1, h, bin_edges)
            s1: the points sampled with the current pdf. The number of points is equal to the dimension of random_in_0_1,
            h: the array with the histogram values at the bin edges,
            bin_edges: the bin edges.

        """
        if not seed is None:
            rng = numpy.random.default_rng(seed)
            cdf_rand_array = rng.random(npoints)
        else:
            cdf_rand_array = numpy.random.random(npoints)
        return self.get_sampled_and_histogram(cdf_rand_array,bins=bins,range=range)

    def _set_default_pdf_x(self):
        self._pdf_x = numpy.arange(self._pdf.size)

    def _get_index(self,edge):
        try:
            ix = numpy.nonzero(self._cdf >= edge)[0][0]
        except:
            ix = 0

        if ix > 0:
            ix -= 1

        if ix >= (self._cdf.size - 1):
            pendent = 0.0
            delta = 0.0
        else:
            pendent = self._cdf[ix + 1] - self._cdf[ix]
            delta = (edge - self._cdf[ix]) / pendent

        return ix//self._cdf_interpolation_factor,delta,pendent


################################################
class S4WigglerLightSource(S4LightSource):
    """
    Defines a wiggler light source and implements the mechanism of sampling rays.

    Parameters
    ----------
    name : str, optional
        The name of the light source.
    electron_beam : instance of ElectronBeam
        The electron beam parameters.
    magnetic_structure : instance of S4BendingMagnet
        The shadow4 bending magnet magnetic structure.
    nrays : int, optional
        The number of rays.
    seed : int, optional
        The Monte Carlo seed.
    """
    def __init__(self,
                 name="Undefined",
                 electron_beam=None,
                 magnetic_structure=None,
                 nrays=5000,
                 seed=12345,
                 ):
        super().__init__(name,
                         electron_beam=electron_beam if not electron_beam is None else S4ElectronBeam(),
                         magnetic_structure=magnetic_structure if not magnetic_structure is None else S4Wiggler(),
                         nrays=nrays,
                         seed=seed)

        # results of calculations
        self.__result_trajectory = None
        self.__result_parameters = None
        self.__result_cdf = None


    def get_trajectory(self):
        """
        Returns the electron trajectory.

        Returns
        -------
        tuple
            (trajectory, parameters) with trajectory a numpy array (8, npoints) and parameters a str.
        """
        if self.__result_trajectory is None: self.__calculate_trajectory()
        return self.__result_trajectory, self.__result_parameters

    def __calculate_trajectory(self):

        wiggler = self.get_magnetic_structure()
        electron_beam = self.get_electron_beam()

        if wiggler._magnetic_field_periodic == 1:

            (traj, pars) = wiggler_trajectory(b_from=0,
                                                     inData="",
                                                     nPer=wiggler.number_of_periods(),
                                                     nTrajPoints=wiggler._NG_J,
                                                     ener_gev=electron_beam._energy_in_GeV,
                                                     per=wiggler.period_length(),
                                                     kValue=wiggler.K_vertical(),
                                                     trajFile="",
                                                     shift_x_flag=wiggler._shift_x_flag,
                                                     shift_x_value=wiggler._shift_x_value,
                                                     shift_betax_flag=wiggler._shift_betax_flag,
                                                     shift_betax_value=wiggler._shift_betax_value, )

        elif wiggler._magnetic_field_periodic == 0:

            (traj, pars) = wiggler_trajectory(b_from=1,
                                                     inData=wiggler._file_with_magnetic_field,
                                                     nPer=1,
                                                     nTrajPoints=wiggler._NG_J,
                                                     ener_gev=electron_beam._energy_in_GeV,
                                                     # per=self.syned_wiggler.period_length(),
                                                     # kValue=self.syned_wiggler.K_vertical(),
                                                     trajFile="",
                                                     shift_x_flag       = wiggler._shift_x_flag     ,
                                                     shift_x_value      = wiggler._shift_x_value    ,
                                                     shift_betax_flag   = wiggler._shift_betax_flag ,
                                                     shift_betax_value  = wiggler._shift_betax_value,)


        self.__result_trajectory = traj
        self.__result_parameters = pars


    def __calculate_radiation(self):

        wiggler = self.get_magnetic_structure()

        if self.__result_trajectory is None: self.__calculate_trajectory()

        #
        # calculate cumulative distribution function
        #
        self.__result_cdf = wiggler_cdf(self.__result_trajectory,
                                        enerMin=wiggler._EMIN,
                                        enerMax=wiggler._EMAX,
                                        enerPoints=1 if wiggler.is_monochromatic() else wiggler._NG_E,
                                        outFile="",
                                        elliptical=False)

    def __psi_max_estimation(self, RAD_MIN, photon_energy, gamma):
        #
        # calculate a "reasonable" uniform vertical divergence (psi) array that will accept all radiation
        # It uses a fit that can be found at: shadow4-tests/shadow4tests/devel/fit_psi_interval.py
        #
        m2ev = codata.c * codata.h / codata.e
        TOANGS = m2ev * 1e10

        RAD_MIN = 1.0 / numpy.abs(self.__result_cdf["curv"]).max()
        critical_energy = TOANGS * 3.0 * numpy.power(gamma, 3) / 4.0 / numpy.pi / 1.0e10 * (1.0 / RAD_MIN)
        print(">>>>>> RAD_MIN, critical_energy: ", RAD_MIN, critical_energy)
        c = numpy.array([-0.3600382, 0.11188709])  # see file fit_psi_interval.py
        # x = numpy.log10(self._EMIN / critical_energy)
        x = numpy.log10(photon_energy / (4 * critical_energy)) # the wiggler that does not have an unique
                                                            # Ec. To be safe, I use 4 times the
                                                            # Ec vale to make the interval wider than for the BM
        y_fit = c[1] + c[0] * x
        psi_interval_in_units_one_over_gamma = 10 ** y_fit  # this is the semi interval
        psi_interval_in_units_one_over_gamma *= 4  # doubled interval
        if psi_interval_in_units_one_over_gamma < 2:
            psi_interval_in_units_one_over_gamma = 2

        return psi_interval_in_units_one_over_gamma

    def __calculate_rays(self,user_unit_to_m=1.0,F_COHER=0,EPSI_DX=0.0,EPSI_DZ=0.0,
                       psi_interval_in_units_one_over_gamma=None,
                       psi_interval_number_of_points=1001,
                       verbose=True):
        # compute the rays in SHADOW matrix (shape (npoints,18) )
        # :param F_COHER: set this flag for coherent beam
        # :param user_unit_to_m: default 1.0 (m)
        # :return: rays, a numpy.array((npoits,18))
        if self.__result_cdf is None:
            self.__calculate_radiation()

        if verbose:
            print(">>>   Results of calculate_radiation")
            print(">>>       trajectory.shape: ", self.__result_trajectory.shape)
            print(">>>       cdf: ", self.__result_cdf.keys())

        wiggler = self.get_magnetic_structure()
        syned_electron_beam = self.get_electron_beam()



        ###############################################
        gamma = syned_electron_beam.gamma()
        m2ev = codata.c * codata.h / codata.e
        TOANGS = m2ev * 1e10
        NRAYS = self.get_nrays()
        sigmas = syned_electron_beam.get_sigmas_all()
        #####################################################


        if self.get_seed() != 0:
            numpy.random.seed(self.get_seed())

        t0 = time.time()
        if wiggler._FLAG_EMITTANCE:
            if numpy.array(numpy.abs(sigmas)).sum() == 0:
                wiggler._FLAG_EMITTANCE = False


        #
        # sample sizes (cols 1-3)
        #

        PATH_STEP = self.__result_cdf["step"]
        X_TRAJ    = self.__result_cdf["x"]
        Y_TRAJ    = self.__result_cdf["y"]
        SEEDIN    = self.__result_cdf["cdf"]
        ANGLE     = self.__result_cdf["angle"]
        CURV      = self.__result_cdf["curv"]
        EPSI_PATH = numpy.arange(CURV.size) * PATH_STEP # should be like Y_TRAJ - Y_TRAJ[0]

        if False:
            print(">>>>> PATH_STEP: ", PATH_STEP, Y_TRAJ[1] - Y_TRAJ[0]) # todo: check preprocessor: PATH_STEP:  0.001000019065427119 0.0010000000000000009
            from srxraylib.plot.gol import plot
            plot(Y_TRAJ, X_TRAJ, xtitle='y', ytitle='x', title="trajectory", show=0)
            plot(Y_TRAJ, SEEDIN, xtitle='y', ytitle='cdf', title="cdf", show=0)
            plot(Y_TRAJ, ANGLE, xtitle='y', ytitle="x'", title="angle", show=0)
            plot(Y_TRAJ, CURV, xtitle='y', ytitle="1/R", title="curvature", show=0)
            plot(Y_TRAJ, EPSI_PATH, Y_TRAJ, Y_TRAJ-Y_TRAJ[0], xtitle='y', ytitle="epsi path", title="epsi path", show=1)

        # ! C We define the 5 arrays:
        # ! C    Y_X(5,N)    ---> X(Y)
        # ! C    Y_XPRI(5,N) ---> X'(Y)
        # ! C    Y_CURV(5,N) ---> CURV(Y)
        # ! C    Y_PATH(5,N) ---> PATH(Y)
        # ! C    F(1,N) contains the array of Y values where the nodes are located.

        # CALL PIECESPL(SEED_Y, Y_TEMP,   NP_SY,   IER)
        # CALL CUBSPL (Y_X,    X_TEMP,   NP_TRAJ, IER)
        # CALL CUBSPL (Y_Z,    Z_TEMP,   NP_TRAJ, IER)
        # CALL CUBSPL (Y_XPRI, ANG_TEMP, NP_TRAJ, IER)
        # CALL CUBSPL (Y_ZPRI, ANG2_TEMP, NP_TRAJ, IER)
        # CALL CUBSPL (Y_CURV, C_TEMP,   NP_TRAJ, IER)
        # CALL CUBSPL (Y_PATH, P_TEMP,   NP_TRAJ, IER)

        SEED_Y = interp1d(SEEDIN, Y_TRAJ,    kind='linear')
        Y_X    = interp1d(Y_TRAJ, X_TRAJ,    kind='cubic')
        Y_XPRI = interp1d(Y_TRAJ, ANGLE,     kind='cubic')
        Y_CURV = interp1d(Y_TRAJ, CURV,      kind='cubic')
        Y_PATH = interp1d(Y_TRAJ, EPSI_PATH, kind='cubic')

        # ! C Compute the path length to the middle (origin) of the wiggler.
        # ! C We need to know the "center" of the wiggler coordinate.
        # ! C input:     Y_PATH  ---> spline array
        # ! C            NP_TRAJ ---> # of points
        # ! C            Y_TRAJ  ---> calculation point (ind. variable)
        # ! C output:    PATH0   ---> value of Y_PATH at X = Y_TRAJ. If
        # ! C                         Y_TRAJ = 0, then PATH0 = 1/2 length
        # ! C                         of trajectory.

        # Y_TRAJ = 0.0
        # # CALL SPL_INT (Y_PATH, NP_TRAJ, Y_TRAJ, PATH0, IER)
        # PATH0 = Y_PATH(Y_TRAJ)
        PATH0 = Y_PATH(0.0)

        #
        # calculate a "reasonable" uniform vertical divergence (psi) array that will accept all radiation
        #
        if psi_interval_in_units_one_over_gamma is None:
            RAD_MIN = 1.0 / numpy.abs(self.__result_cdf["curv"]).max()
            psi_interval_in_units_one_over_gamma = self.__psi_max_estimation(RAD_MIN, wiggler._EMIN, gamma)

            # critical_energy = TOANGS * 3.0 * numpy.power(gamma, 3) / 4.0 / numpy.pi / 1.0e10 * (1.0 / RAD_MIN)
            # print(">>>>>> RAD_MIN, critical_energy: ", RAD_MIN, critical_energy)
            # c = numpy.array([-0.3600382, 0.11188709])  # see file fit_psi_interval.py
            # # x = numpy.log10(self._EMIN / critical_energy)
            # x = numpy.log10(wiggler._EMIN / (4 * critical_energy)) # the wiggler that does not have an unique
            #                                                     # Ec. To be safe, I use 4 times the
            #                                                     # Ec vale to make the interval wider than for the BM
            # y_fit = c[1] + c[0] * x
            # psi_interval_in_units_one_over_gamma = 10 ** y_fit  # this is the semi interval
            # psi_interval_in_units_one_over_gamma *= 4  # doubled interval
            # if psi_interval_in_units_one_over_gamma < 2:
            #     psi_interval_in_units_one_over_gamma = 2

        if verbose:
            print(">>> psi_interval_in_units_one_over_gamma: ",psi_interval_in_units_one_over_gamma)

        angle_array_mrad = numpy.linspace(-0.5*psi_interval_in_units_one_over_gamma * 1e3 / gamma,
                                          0.5*psi_interval_in_units_one_over_gamma * 1e3 / gamma,
                                          psi_interval_number_of_points)

        a = angle_array_mrad
        a8 = 1.0
        hdiv_mrad = 1.0

        #
        ####################  SAMPLING ##################
        #

        t1 = time.time()
        rays = numpy.zeros((NRAYS, 18))

        #
        # sampling energies
        #
        if wiggler.is_monochromatic():
            sampled_energies = numpy.ones(NRAYS) * wiggler._EMIN
        else:
            ws_ev, ws_f, _ =  wiggler_spectrum(self.__result_trajectory,
                                               enerMin=wiggler._EMIN,
                                               enerMax=wiggler._EMAX,
                                               nPoints=500,
                                               # per=self.syned_wiggler.period_length(),
                                               electronCurrent=syned_electron_beam._current,
                                               outFile="",
                                               elliptical=False)



            ws_flux_per_ev = ws_f / (ws_ev * 1e-3)

            samplerE = Sampler1D(ws_flux_per_ev, ws_ev)

            sampled_energies, _, _ = samplerE.get_n_sampled_points_and_histogram(NRAYS)

        t11 = time.time()

        #
        # sample sizes
        # note that sizes are not depending on the photon energy, only on the electron trajectory and emittance.
        #

        #
        # sample x,y coordinates along the x(y) trajectory and the corresponding
        # transversal angle x' and curvature
        #
        arg_y_array     = numpy.random.random(NRAYS)
        Y_TRAJ_array    = SEED_Y(arg_y_array)
        X_TRAJ_array    = Y_X(Y_TRAJ_array)
        ANGLE_array     = Y_XPRI(Y_TRAJ_array)
        CURV_array      = Y_CURV(Y_TRAJ_array)
        EPSI_PATH_array = Y_PATH(Y_TRAJ_array)

        if False:
            from srxraylib.plot.gol import plot
            plot(Y_TRAJ, X_TRAJ,
                Y_TRAJ_array, X_TRAJ_array,
                 marker=[None,'.'], linestyle=[None,""], legend=['data', 'sampled'], show=1)
            plot(Y_TRAJ_array, sampled_energies,
                 marker='.', linestyle="", xtitle='y', ytitle="photon energy", show=1)

        #
        # sample coordinates from electron beam
        #
        E_BEAMXXX_array = numpy.zeros(NRAYS)
        E_BEAM1_array = numpy.zeros(NRAYS)
        E_BEAMZZZ_array = numpy.zeros(NRAYS)
        E_BEAM3_array = numpy.zeros(NRAYS)

        t2 = time.time()
        if wiggler._FLAG_EMITTANCE:
            sigmaX, sigmaXp, sigmaZ, sigmaZp = syned_electron_beam.get_sigmas_all()
            meanX = [0, 0]
            meanZ = [0, 0]
            rSigmaXp = sigmaXp
            rSigmaZp = sigmaZp

            for itik in range(NRAYS):
                EPSI_PATH = EPSI_PATH_array[itik] - PATH0  # now refer to wiggler's origin
                # ! C
                # ! C Compute the actual distance (EPSI_W*) from the orbital focus
                # ! C
                EPSI_WX = EPSI_DX + EPSI_PATH
                EPSI_WZ = EPSI_DZ + EPSI_PATH

                rSigmaX = numpy.sqrt((EPSI_WX ** 2) * (sigmaXp ** 2) + sigmaX ** 2)
                rSigmaZ = numpy.sqrt((EPSI_WZ ** 2) * (sigmaZp ** 2) + sigmaZ ** 2)
                rhoX = EPSI_WX * sigmaXp ** 2 / (rSigmaX * rSigmaXp)
                rhoZ = EPSI_WZ * sigmaZp ** 2 / (rSigmaZ * rSigmaZp)
                covX = [[sigmaX ** 2, rhoX * sigmaX * sigmaXp],
                        [rhoX * sigmaX * sigmaXp, sigmaXp ** 2]]  # diagonal covariance

                covZ = [[sigmaZ ** 2, rhoZ * sigmaZ * sigmaZp],
                        [rhoZ * sigmaZ * sigmaZp, sigmaZp ** 2]]  # diagonal covariance

                # sampling using a multivariare (2) normal distribution
                # multivariate_normal is very slow.
                # See https://github.com/numpy/numpy/issues/14193 and shadow4-tests/shadow4tests/devel/check_multivariate_normal.py
                # for acceleration recipee. For 5k rays this emittance loop passed from 31% to 8% of the total time.
                # sampled_x, sampled_xp = numpy.random.multivariate_normal(meanX, covX, 1).T
                # sampled_z, sampled_zp = numpy.random.multivariate_normal(meanZ, covZ, 1).T
                sampled_x, sampled_xp = (meanX + numpy.linalg.cholesky(covX) @ numpy.random.standard_normal(len(meanX))).T
                sampled_z, sampled_zp = (meanZ + numpy.linalg.cholesky(covZ) @ numpy.random.standard_normal(len(meanZ))).T

                XXX = sampled_x
                ZZZ = sampled_z

                E_BEAM1 = sampled_xp
                E_BEAM3 = sampled_zp

                E_BEAM1_array[itik] = E_BEAM1
                E_BEAM3_array[itik] = E_BEAM3
                E_BEAMXXX_array[itik] = XXX
                E_BEAMZZZ_array[itik] = ZZZ

        t3 = time.time()

        #
        # sample sizes
        #
        do_loop = 0

        if do_loop:
            for itik in range(NRAYS):


                Y_TRAJ = Y_TRAJ_array[itik]


                X_TRAJ = X_TRAJ_array[itik]
                ANGLE = ANGLE_array[itik]
                CURV = CURV_array[itik]
                EPSI_PATH = EPSI_PATH_array[itik] - PATH0 # now refer to wiggler's origin

                if CURV < 0:
                    POL_ANGLE = numpy.radians(90.0) # instant orbit is CW
                else:
                    POL_ANGLE = numpy.radians(-90.0) # CCW

                if CURV == 0.0:
                    R_MAGNET = 1.0e20
                else:
                    R_MAGNET = numpy.abs(1.0 / CURV)


                # retrieve the electron sampled values
                ANGLE = ANGLE_array[itik]
                XXX = E_BEAMXXX_array[itik]
                E_BEAM1 = E_BEAM1_array[itik]
                ZZZ = E_BEAMZZZ_array[itik]
                E_BEAM3 = E_BEAM3_array[itik]

                # ! C For normal wiggler, XXX is perpendicular to the electron trajectory at
                # ! C the point defined by (X_TRAJ,Y_TRAJ,0).

                YYY = Y_TRAJ - XXX * numpy.sin(ANGLE)
                XXX = X_TRAJ + XXX * numpy.cos(ANGLE)

                rays[itik,0] = XXX
                rays[itik,1] = YYY
                rays[itik,2] = ZZZ
        else:

            # EPSI_PATH = EPSI_PATH_array - PATH0  # now refer to wiggler's origin
            POL_ANGLE_array = numpy.radians(-90.0 * numpy.sign(CURV_array))

            R_MAGNET_array = numpy.abs(1.0 / CURV_array)
            ibad = numpy.argwhere( numpy.abs(CURV_array) < 1e-10)
            R_MAGNET_array[ibad] = 1.0e20

            ZZZ = E_BEAMZZZ_array
            YYY = X_TRAJ_array - E_BEAMXXX_array * numpy.sin(ANGLE_array)
            XXX = X_TRAJ_array + E_BEAMXXX_array * numpy.cos(ANGLE_array)

            rays[:, 0] = XXX
            rays[:, 1] = YYY
            rays[:, 2] = ZZZ

        t4 = time.time()

        #
        # divergences
        #

        RAD_MIN_array = numpy.abs(R_MAGNET_array)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # calculate the sampled_theta, sampled_photon_energy and sampled_polarization.
        method = 'old'

        if method == 'new' or method == 'old':

            # sampled_photon_energy = sampled_energies[0]
            critical_energy_array = TOANGS * 3.0 * numpy.power(gamma, 3) / 4.0 / numpy.pi / 1.0e10 * (1.0 / RAD_MIN_array)
            # print(">>>>>>>>>>>>>>> critical energy: ", critical_energy.min(), critical_energy.max(), critical_energy)
            eene = sampled_energies / critical_energy_array
            # print(">>>>>>>>>>>>>>> eene: ", eene.min(), eene.max(), eene)

            e_over_ec_array_points = 101
            e_over_ec_array = numpy.linspace(eene.min(), eene.max(), e_over_ec_array_points)

            angular_array_reduced = angle_array_mrad * 1e-3 * gamma

            AA = numpy.outer(angular_array_reduced, numpy.ones_like(e_over_ec_array))
            EE = numpy.outer(numpy.ones_like(angular_array_reduced), e_over_ec_array)

            fm_s, fm_p = sync_f_sigma_and_pi(AA, EE)
            # print(">>>>>>>>>>>>>>> fm_s, fm_p: ", fm_s.shape, fm_p.shape, AA.shape, EE.shape)
            cte = EE ** 2 * a8 * syned_electron_beam._current * hdiv_mrad * syned_electron_beam._energy_in_GeV ** 2
            fm_s *= cte
            fm_p *= cte
            fm = fm_s + fm_p
            fm_pol = numpy.sqrt(fm_s) / (numpy.sqrt(fm_s) + numpy.sqrt(fm_p))

            if False:
                from srxraylib.plot.gol import plot_image
                plot_image(fm, angular_array_reduced, e_over_ec_array, title='intensity', xtitle='reduced angle', ytitle='reduced energy', aspect='auto')

            if False:
                from srxraylib.plot.gol import plot_image
                plot_image(fm_pol, angular_array_reduced, e_over_ec_array, title='polarization', xtitle='reduced angle', ytitle='reduced energy', aspect='auto')


            # samplerAAEE = Sampler2D(fm, AA, EE)
            # cdf2, cdf1 = samplerAAEE.cdf()

            interpolators = []
            cdf1d = numpy.zeros_like(fm)

            for i in range(e_over_ec_array.size):
                interpolators.append( Sampler1D(fm[:,i], angular_array_reduced) )
                cdf1d[:, i] = interpolators[-1].cdf()

            if True:
                from srxraylib.plot.gol import plot, plot_image
                plot_image(cdf1d, angular_array_reduced, e_over_ec_array, xtitle='reduced angle',
                           ytitle='reduced energy', title='cdf1d', aspect='auto')


            Pi = numpy.array([AA.flatten(), EE.flatten()]).transpose()
            # print(">>>>>>>>>>>>>>>> Pi", Pi.shape, cdf1d.flatten().shape)
            interpolator = LinearNDInterpolator(Pi, cdf1d.flatten(), fill_value=0.0, rescale=True)

            # interpolator_polarization = LinearNDInterpolator(Pi, fm_pol.flatten(), fill_value=0.0, rescale=True)
            interpolator_polarization = CloughTocher2DInterpolator(Pi, fm_pol.flatten(), fill_value=0.0, rescale=True)

            # pol_deg_interpolator = interp1d(angle_array_mrad * 1e-3,
            #         numpy.sqrt(angular_distribution_s) / (numpy.sqrt(angular_distribution_s) + numpy.sqrt(angular_distribution_p)))
            # sampled_polarization = pol_deg_interpolator(sampled_angle)

            # eeee = eene.max() # e_over_ec_array[5]
            # cdf_interpolated = interpolator(angular_array_reduced, eeee)
            # plot(angular_array_reduced, cdf_interpolated, title='E/Ec=%f' % eeee)



            # # Pi = numpy.array([Angle_array_mrad.flatten() * 1e-3, Photon_energy_array.flatten()]).transpose()
            # Pi = numpy.array([AA.flatten(), EE.flatten()]).transpose()
            # print(">>>>>>>>>>>>>>>> Pi", Pi.shape, cdf2.flatten().shape)
            # # polarization_degree = numpy.sqrt(fm_s) / (numpy.sqrt(fm_s) + numpy.sqrt(fm_p))
            #
            # # interpolator = CloughTocher2DInterpolator(Pi, cdf2.flatten(), fill_value=0.0, rescale=True)
            # interpolator = LinearNDInterpolator(Pi, cdf2.flatten(), fill_value=0.0, rescale=True)
            # # sampled_polarization = interpolator(sampled_angle, sampled_photon_energy)
            # eeee = numpy.ones_like(angular_array_reduced) * e_over_ec_array[10]
            # cdf_interpolated = interpolator(angular_array_reduced, eeee)
            #
            # # for i in range(eeee.size):
            # #     print(i, angular_array_reduced[i], eeee[i], cdf_interpolated[i])
            #
            # if True:
            #     from srxraylib.plot.gol import plot, plot_image
            #     plot_image(cdf2, angular_array_reduced, e_over_ec_array, xtitle='reduced angle',
            #                ytitle='reduced energy', title='cdf2', aspect='auto')
            #
            #     plot(angular_array_reduced, cdf_interpolated)
            #
            # print(">>> cdf: ", cdf2.shape, cdf1.shape)
            #
            # plot(angular_array_reduced, fm[:, 5], title='1D PDF')
            # :
            # print(sampler1d.cdf())
            # plot(angular_array_reduced, sampler1d.cdf(), title='1D CDF')





            # eene = eene[0] #!!!!!!!!!!!!!!!!!!!!!!!!!!
            #
            #
            # fm_pol = numpy.zeros_like(fm)
            # for i in range(fm_pol.size):
            #     if fm[i] == 0.0:
            #         fm_pol[i] = 0
            #     else:
            #         # folowing the bug fixed for BM, this should also be changed.
            #         # fm_pol[i] = fm_s[i] / fm[i]
            #         fm_pol[i] = numpy.sqrt(fm_s[i]) / (numpy.sqrt(fm_s[i]) + numpy.sqrt(fm_p[i]))
            #
            # fm.shape = -1
            # fm_s.shape = -1
            # fm_pol.shape = -1
            #
            # pol_deg_interpolator = interp1d(a * 1e-3, fm_pol)
            #
            # samplerAng = Sampler1D(fm, a * 1e-3)
            #
            # # samplerPol = Sampler1D(fm_s/fm,a*1e-3)
            #
            # # plot(a*1e-3,fm_s/fm)
            #
            # if fm.min() == fm.max():
            #     print("Warning: cannot compute divergence for ray index %d" % itik)
            #     sampled_theta = 0.0
            # else:
            #     ARG_ENER = numpy.random.random(NRAYS)
            #     sampled_theta = samplerAng.get_sampled(ARG_ENER)
            #
            # sampled_pol_deg = pol_deg_interpolator(sampled_theta)


            # e_gev = self.get_electron_beam().energy()
            # i_a = self.get_electron_beam().current()
            # hdiv_mrad = (HDIV1 + HDIV2) * 1e3
            # energy = self.get_magnetic_structure()._EMIN
            # ec_ev = critical_energy
            #
            # angle_mrad = angle_array_mrad
            # codata_mee = 1e-6 * codata.m_e * codata.c ** 2 / codata.e
            #
            # eene = energy / ec_ev
            # gamma = e_gev * 1e3 / codata_mee
            # angular_distribution_s, angular_distribution_p = sync_f_sigma_and_pi(angle_mrad * gamma / 1e3, eene)
            #
            # a8 = codata.e / numpy.power(codata_mee, 2) / codata.h * (9e-2 / 2 / numpy.pi) # a8 = 1.3264d13
            # angular_distribution_s *= eene**2 * a8 * i_a * hdiv_mrad * e_gev**2
            # angular_distribution_p *= eene**2 * a8 * i_a * hdiv_mrad * e_gev**2
            #
            # sampler_angle = Sampler1D(angular_distribution_s + angular_distribution_p, angle_array_mrad * 1e-3)
            # sampled_angle = sampler_angle.get_n_sampled_points(NRAYS)
            #
            # pol_deg_interpolator = interp1d(angle_array_mrad * 1e-3,
            #         numpy.sqrt(angular_distribution_s) / (numpy.sqrt(angular_distribution_s) + numpy.sqrt(angular_distribution_p)))
            # sampled_polarization = pol_deg_interpolator(sampled_angle)
            #
            # sampled_photon_energy = numpy.zeros_like(sampled_angle) + self.get_magnetic_structure()._EMIN



        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        t44 = time.time()
        for itik in range(NRAYS):

            ############################################# copier from previous
            POL_ANGLE = POL_ANGLE_array[itik]
            R_MAGNET = R_MAGNET_array[itik]
            ANGLE = ANGLE_array[itik]
            #############################################
            #
            # directions
            #

            #     ! C
            #     ! C Synchrotron source
            #     ! C Note. The angle of emission IN PLANE is the same as the one used
            #     ! C before. This will give rise to a source curved along the orbit.
            #     ! C The elevation angle is instead characteristic of the SR distribution.
            #     ! C The electron beam emittance is included at this stage. Note that if
            #     ! C EPSI = 0, we'll have E_BEAM = 0.0, with no changes.
            #     ! C
            #     IF (F_WIGGLER.EQ.3) ANGLE=0        ! Elliptical Wiggler.
            #     ANGLEX =   ANGLE + E_BEAM(1)
            #     DIREC(1)  =   TAN(ANGLEX)
            #     IF (R_ALADDIN.LT.0.0D0) DIREC(1) = - DIREC(1)
            #     DIREC(2)  =   1.0D0
            #     ARG_ANG  =   GRID(6,ITIK)

            ANGLEX = ANGLE + E_BEAM1
            DIREC1 = numpy.tan(ANGLEX)
            DIREC2 = 1.0


            #     ! C In the case of SR, we take into account the fact that the electron
            #     ! C trajectory is not orthogonal to the field. This will give a correction
            #     ! C to the photon energy.  We can write it as a correction to the
            #     ! C magnetic field strength; this will linearly shift the critical energy
            #     ! C and, with it, the energy of the emitted photon.


            E_TEMP3 = numpy.tan(E_BEAM3)/numpy.cos(E_BEAM1)
            E_TEMP2 = 1.0
            E_TEMP1 = numpy.tan(E_BEAM1)

            e_temp_norm = numpy.sqrt( E_TEMP1**2 + E_TEMP2**2 + E_TEMP3**2)

            E_TEMP3 /= e_temp_norm
            E_TEMP2 /= e_temp_norm
            E_TEMP1 /= e_temp_norm

            CORREC = numpy.sqrt(1.0 - E_TEMP3**2) # todo: double-check why we do not use CORREC


            #     IF (FDISTR.EQ.6) THEN
            #         CALL ALADDIN1 (ARG_ANG,ANGLEV,F_POL,IER)
            #         Q_WAVE =   TWOPI*PHOTON(1)/TOCM*CORREC
            #         POL_DEG =   ARG_ANG
            #     ELSE IF (FDISTR.EQ.4) THEN
            #         ARG_ENER =   WRAN (ISTAR1)
            #         RAD_MIN =   ABS(R_MAGNET)
            #
            #         i1 = 1
            #         CALL WHITE  &
            #         (RAD_MIN,CORREC,ARG_ENER,ARG_ANG,Q_WAVE,ANGLEV,POL_DEG,i1)
            #     END IF



            if method == 'new':
                # raise Exception("Not implemented")
                sampled_photon_energy = sampled_energies[itik]
                ########################################################
                e_index = numpy.argwhere((e_over_ec_array - sampled_photon_energy / critical_energy_array[itik]) > 0)
                print(">>>>>>>>> e_index: ", e_index[0][0], critical_energy_array[itik] * e_over_ec_array[e_index[0][0]], critical_energy_array[itik] * e_over_ec_array[1+e_index[0][0]])
                # e_index = e_index[0]
                # print(">>>>>>>>> e_index: ", e_index)

                print(">>>>>>>>>>reduced energy, energy: ", sampled_photon_energy / critical_energy_array[itik], sampled_photon_energy)
                cdf_interpolated = interpolator(angular_array_reduced, sampled_photon_energy / critical_energy_array[itik])
                s = Sampler1Dcdf(cdf_interpolated, angle_array_mrad)
                r = numpy.random.random()
                sampled_theta = s.get_sampled(r) * 1e-3
                print("        >>>>>>>>>>reduced sampled_theta: ", sampled_theta)
                sampled_pol_deg = interpolator_polarization(sampled_theta * gamma, sampled_photon_energy  / critical_energy_array[itik])

                if True:
                    from srxraylib.plot.gol import plot
                    plot(angular_array_reduced, cdf_interpolated,
                         [sampled_theta * gamma, sampled_theta * gamma], [0.5, 0.6],
                         title="Energy: %f" % sampled_photon_energy)
                ########################################################
            else:
                # RAD_MIN = numpy.abs(R_MAGNET)
                # wavelength = codata.h * codata.c / codata.e /sampled_photon_energy
                # critical_energy = TOANGS * 3.0 * numpy.power(gamma, 3) / 4.0 / numpy.pi / 1.0e10 * (1.0 / RAD_MIN)
                RAD_MIN = RAD_MIN_array[itik]  # numpy.abs(R_MAGNET)
                sampled_photon_energy = sampled_energies[itik]
                critical_energy = critical_energy_array[itik]

                eene = sampled_photon_energy / critical_energy

                fm_s , fm_p = sync_f_sigma_and_pi(a * 1e-3 * syned_electron_beam.gamma(), eene)
                cte = eene ** 2 * a8 * syned_electron_beam._current * hdiv_mrad * syned_electron_beam._energy_in_GeV ** 2
                fm_s *= cte
                fm_p *= cte

                fm = fm_s + fm_p

                fm_pol = numpy.zeros_like(fm)
                for i in range(fm_pol.size):
                    if fm[i] == 0.0:
                        fm_pol[i] = 0
                    else:
                        fm_pol[i] = numpy.sqrt(fm_s[i]) / (numpy.sqrt(fm_s[i]) + numpy.sqrt(fm_p[i]))

                fm.shape = -1
                fm_s.shape = -1
                fm_pol.shape = -1

                pol_deg_interpolator = interp1d(a*1e-3,fm_pol)

                samplerAng = Sampler1D(fm, a * 1e-3)

                if fm.min() == fm.max():
                    print("Warning: cannot compute divergence for ray index %d" % itik)
                    sampled_theta = 0.0
                else:
                    ARG_ENER = numpy.random.random()
                    sampled_theta = samplerAng.get_sampled(ARG_ENER)

                sampled_pol_deg = pol_deg_interpolator(sampled_theta)

                if False:
                    from srxraylib.plot.gol import plot
                    plot(a*1e-3, samplerAng.cdf(),
                         [sampled_theta, sampled_theta], [0.5, 0.6],
                         title="Energy: %f" % sampled_photon_energy)

                ######################################################## NEW ####################################
                e_index = numpy.argwhere((e_over_ec_array - sampled_photon_energy / critical_energy) > 0)
                print(">>>>>>>>> e_index: ", e_index[0][0], critical_energy * e_over_ec_array[e_index[0][0]], critical_energy * e_over_ec_array[1+e_index[0][0]])
                # e_index = e_index[0]
                # print(">>>>>>>>> e_index: ", e_index)

                print(">>>>>>>>>>reduced energy, energy: ", sampled_photon_energy / critical_energy, sampled_photon_energy)
                cdf_interpolated = interpolator(angular_array_reduced, sampled_photon_energy / critical_energy)
                s = Sampler1Dcdf(cdf_interpolated, angle_array_mrad)
                r = numpy.random.random()
                sampled_theta1 = s.get_sampled(r) * 1e-3
                print("        >>>>>>>>>>reduced sampled_theta1: ", sampled_theta1)
                sampled_pol_deg1 = interpolator_polarization(sampled_theta1 * gamma, sampled_photon_energy  / critical_energy)

                if True:
                    from srxraylib.plot.gol import plot
                    plot(angular_array_reduced, cdf_interpolated,
                         [sampled_theta1 * gamma, sampled_theta1 * gamma], [0.5, 0.6],
                         numpy.linspace(-0.5 * psi_interval_in_units_one_over_gamma,
                                        0.5 * psi_interval_in_units_one_over_gamma,
                                        psi_interval_number_of_points),
                         samplerAng.cdf(),
                         [sampled_theta * gamma, sampled_theta * gamma], [0.6, 0.7],
                         title="Energy: %f" % sampled_photon_energy,
                         marker=['+', None, None, None],
                         legend=['new','new','old','old'])
                ######################################################## END NEW ##################################
            ###################################################################################################################

            # print("sampled_theta: ",sampled_theta, "sampled_energy: ",sampled_photon_energy, "sampled pol ",sampled_pol_deg)

            ANGLEV = sampled_theta
            ANGLEV += E_BEAM3
            #     IF (ANGLEV.LT.0.0) I_CHANGE = -1
            #     ANGLEV =   ANGLEV + E_BEAM(3)
            #     ! C
            #     ! C Test if the ray is within the specified limits
            #     ! C
            #     IF (FGRID.EQ.0.OR.FGRID.EQ.2) THEN
            #         IF (ANGLEV.GT.VDIV1.OR.ANGLEV.LT.-VDIV2) THEN
            #             ARG_ANG = WRAN(ISTAR1)
            #             ! C
            #             ! C If it is outside the range, then generate another ray.
            #             ! C
            #             GO TO 4400
            #         END IF
            #     END IF
            #     DIREC(3)  =   TAN(ANGLEV)/COS(ANGLEX)

            DIREC3 = numpy.tan(ANGLEV) / numpy.cos(ANGLEX)
            #     IF (F_WIGGLER.EQ.3) THEN
            #         CALL ROTATE (DIREC, ANGLE3,ANGLE2,ANGLE1,DIREC)
            #     END IF
            #     CALL NORM (DIREC,DIREC)

            direc_norm = numpy.sqrt(DIREC1**2 + DIREC2**2 + DIREC3**2)

            DIREC1 /= direc_norm
            DIREC2 /= direc_norm
            DIREC3 /= direc_norm

            rays[itik,3] = DIREC1 # VX
            rays[itik,4] = DIREC2 # VY
            rays[itik,5] = DIREC3 # VZ

        t5 = time.time() # end loop

        if user_unit_to_m != 1.0:
            rays[:,0] /= user_unit_to_m
            rays[:,1] /= user_unit_to_m
            rays[:,2] /= user_unit_to_m

        #
        # sample divergences (cols 4-6): the Shadow way
        #


        #
        # electric field vectors (cols 7-9, 16-18) and phases (cols 14-15)
        #

        # ! C                 POLARIZATION
        # ! C   Generates the polarization of the ray. This is defined on the
        # ! C   source plane, so that A_VEC is along the X-axis and AP_VEC is along Z-axis.
        # ! C   Then care must be taken so that A will be perpendicular to the ray
        # ! C   direction.
        DIREC = rays[:, 3:6].copy()
        A_VEC = numpy.zeros_like(DIREC)
        A_VEC[:, 0] = 1.0  # A_VEC(1) = 1.0 A_VEC(2) = 0.0 A_VEC(3) = 0.0

        # ! C   Rotate A_VEC so that it will be perpendicular to DIREC and with the
        # ! C   right components on the plane.
        A_TEMP = vector_cross(A_VEC,DIREC)
        A_VEC = vector_cross(DIREC,A_TEMP)
        A_VEC = vector_norm(A_VEC)
        AP_VEC = vector_cross(A_VEC,DIREC)
        AP_VEC = vector_norm(AP_VEC)

        #
        # obtain polarization for each ray (interpolation)
        #
        POL_DEG = sampled_pol_deg
        DENOM = numpy.sqrt(1.0 - 2.0 * POL_DEG + 2.0 * POL_DEG**2)
        AX = POL_DEG/DENOM
        for i in range(3):
            A_VEC[:,i] *= AX

        AZ = (1.0-POL_DEG)/DENOM
        for i in range(3):
            AP_VEC[:,i] *= AZ


        rays[:,6:9] =  A_VEC
        rays[:,15:18] = AP_VEC

        #
        # ! C
        # ! C Now the phases of A_VEC and AP_VEC.
        # ! C

        #
        POL_ANGLE = 0.5 * numpy.pi

        if F_COHER == 1:
            PHASEX = 0.0
        else:
            PHASEX = numpy.random.random(NRAYS) * 2 * numpy.pi

        # PHASEZ = PHASEX + POL_ANGLE * numpy.sign(ANGLEV)

        rays[:,13] = 0.0 # PHASEX
        rays[:,14] = 0.0 # PHASEZ

        # set flag (col 10)
        rays[:,9] = 1.0

        #
        # photon energy (col 11)
        #

        # A2EV = 2.0*numpy.pi/(codata.h*codata.c/codata.e*1e2)
        sampled_photon_energy = sampled_energies
        wavelength = codata.h * codata.c / codata.e /sampled_photon_energy
        Q_WAVE = 2 * numpy.pi / (wavelength*1e2)
        rays[:,10] =  Q_WAVE # sampled_photon_energy * A2EV

        # col 12 (ray index)
        rays[:,11] =  1 + numpy.arange(NRAYS)

        # col 13 (optical path)
        rays[:,12] = 0.0

        t6 = time.time()

        print("------------ timing---------")

        t = t6-t0
        print("            Total: ", t)
        print("            Pre1 (t1-t0)  ",    (t1-t0), 100 * (t1-t0) / t)
        print("            Pre2 (t2-t1): ",    (t2-t1), 100 * (t2-t1) / t)
        print("                 spectrum (t11-t1)  ",   (t11 - t1), 100 * (t11 - t1) / t)
        print("            loop emitt (t3-t2): ",    (t3-t2), 100 * (t3-t2) / t)
        print("            loop sizes (t4-t3): ",    (t4-t3), 100 * (t4-t3) / t)
        print("            divergence (t5-t4): ",    (t5-t4), 100 * (t5-t4) / t)
        print("                 loop (t5-t44)  ",   (t5 - t44), 100 * (t5 - t44) / t)
        print("            post (t6-t5): ",    (t6-t5), 100 * (t6-t5) / t)

        return rays

    def _sample_photon_energy_theta_and_phi(self):

        #
        # sample divergences
        #
        return 0,0,0

    ############################################################################
    #
    ############################################################################
    def get_beam(self):
        """
        Creates the beam as emitted by the wiggler.

        Returns
        -------
        instance od S4beam
        """

        user_unit_to_m = 1.0
        F_COHER = 0
        EPSI_DX = self.get_magnetic_structure()._EPSI_DX
        EPSI_DZ = self.get_magnetic_structure()._EPSI_DZ
        psi_interval_in_units_one_over_gamma = None
        psi_interval_number_of_points = 1001
        verbose = True

        return S4Beam.initialize_from_array(self.__calculate_rays(
            user_unit_to_m=user_unit_to_m,
            F_COHER=F_COHER,
            EPSI_DX=EPSI_DX,
            EPSI_DZ=EPSI_DZ,
            psi_interval_in_units_one_over_gamma=psi_interval_in_units_one_over_gamma,
            psi_interval_number_of_points=psi_interval_number_of_points,
            verbose=verbose))

    def calculate_spectrum(self, output_file=""):
        """
                Calculates the spectrum.

        Parameters
        ----------
        output_file : str, optional
            Name of the file to write the spectrom (use "" for not writing file).
        """
        traj, pars = self.get_trajectory()
        wig = self.get_magnetic_structure()
        e_min, e_max, ne = wig.get_energy_box()
        ring = self.get_electron_beam()
        if traj is not None:
            e, f, w = wiggler_spectrum(traj,
                          enerMin=e_min,
                          enerMax=e_max,
                          nPoints=1 if wig.is_monochromatic() else ne,
                          electronCurrent=ring.current(),
                          outFile=output_file,
                          elliptical=False)
            return e,f,w
        else:
            raise Exception("Cannot compute spectrum")

    def get_info(self):
        """
        Returns the specific information for the wiggler light source.

        Returns
        -------
        str
        """
        electron_beam = self.get_electron_beam()
        magnetic_structure = self.get_magnetic_structure()

        txt = ""
        txt += "-----------------------------------------------------\n"

        txt += "Input Electron parameters: \n"
        txt += "        Electron energy: %f geV\n"%electron_beam.energy()
        txt += "        Electron current: %f A\n"%electron_beam.current()
        if magnetic_structure._FLAG_EMITTANCE:
            sigmas = electron_beam.get_sigmas_all()
            txt += "        Electron sigmaX: %g [um]\n"%(1e6*sigmas[0])
            txt += "        Electron sigmaZ: %g [um]\n"%(1e6*sigmas[2])
            txt += "        Electron sigmaX': %f urad\n"%(1e6*sigmas[1])
            txt += "        Electron sigmaZ': %f urad\n"%(1e6*sigmas[3])

        txt += "Lorentz factor (gamma): %f\n"%electron_beam.gamma()

        txt2 = magnetic_structure.info()
        return (txt + "\n\n" + txt2)

    def to_python_code(self, **kwargs):
        """
        returns the python code for calculating the wiggler source.

        Returns
        -------
        str
            The python code.
        """
        script = ''
        try:
            script += self.get_electron_beam().to_python_code()
        except:
            script += "\n\n#Error retrieving electron_beam code"

        try:
            script += self.get_magnetic_structure().to_python_code()
        except:
            script += "\n\n#Error retrieving magnetic structure code"

        script += "\n\n\n#light source\nfrom shadow4.sources.wiggler.s4_wiggler_light_source import S4WigglerLightSource"
        script += "\nlight_source = S4WigglerLightSource(name='%s',electron_beam=electron_beam,magnetic_structure=source,nrays=%d,seed=%s)" % \
                                                          (self.get_name(),self.get_nrays(),self.get_seed())
        #
        # script += "\n\n\n#beamline\nfrom shadow4.beamline.s4_beamline import S4Beamline"
        # script += "\nbeamline = S4Beamline(light_source=light_source)"
        script += "\nbeam = light_source.get_beam()"
        return script
if __name__ == "__main__":
    from srxraylib.plot.gol import plot_scatter, set_qt
    set_qt()

    # e_min = 5000.0 # 70490.0 #
    # e_max = 100000.0 # 70510.0 #
    # e_min = 70490.0 #
    # e_max = 70510.0 #
    # NRAYS = 5000
    # use_emittances=True
    #
    #
    #
    # wigFile = "xshwig.sha"
    # inData = ""
    #
    # nPer = 5 # 50
    # nTrajPoints = 501
    # ener_gev = 6.04
    # per = 0.040
    # kValue = 7.85
    # trajFile = "tmp.traj"
    # shift_x_flag = 0
    # shift_x_value = 0.0
    # shift_betax_flag = 0
    # shift_betax_value = 0.0
    #
    #
    #
    #
    # #
    # # syned
    # #
    #
    # electron_beam = S4ElectronBeam(energy_in_GeV=6.04,
    #                                energy_spread = 0.0,
    #                                current = 0.2,
    #                                number_of_bunches = 0,
    #                                moment_xx=(400e-6)**2,
    #                                moment_xxp=0.0,
    #                                moment_xpxp=(10e-6)**2,
    #                                moment_yy=(10e-6)**2,
    #                                moment_yyp=0.0,
    #                                moment_ypyp=(4e-6)**2)
    #
    #
    # w = S4Wiggler(K_vertical=kValue,period_length=per,number_of_periods=nPer,
    #                             flag_emittance=use_emittances,
    #                             emin=e_min, emax=e_max,ng_e=10, ng_j=nTrajPoints)
    #
    #
    #
    # # print(w.info())
    #
    # ls = S4WigglerLightSource(name="Undefined", electron_beam=electron_beam, magnetic_structure=w,
    #                           nrays=NRAYS)
    #
    # print(ls.info())
    #
    #
    # beam = ls.get_beam()
    #
    # rays = beam.rays
    #
    # plot_scatter(rays[:,1],rays[:,0],title="trajectory",show=False)
    # plot_scatter(rays[:,0],rays[:,2],title="real space",show=False)
    # plot_scatter(rays[:,3],rays[:,5],title="divergence space")

    # electron beam
    from shadow4.sources.s4_electron_beam import S4ElectronBeam

    electron_beam = S4ElectronBeam(energy_in_GeV=6, energy_spread=0.001, current=0.2)
    electron_beam.set_sigmas_all(sigma_x=2.377e-05, sigma_y=2.472e-05, sigma_xp=3.58e-06, sigma_yp=3.04e-06)

    # magnetic structure
    from shadow4.sources.wiggler.s4_wiggler import S4Wiggler

    source = S4Wiggler(
        magnetic_field_periodic=0,  # 0=external, 1=periodic
        file_with_magnetic_field="/nobackup/gurb1/srio/Oasys/SW_BM18_Joel.txt",  # used only if magnetic_field_periodic=0
        K_vertical=10.0,  # syned Wiggler pars: used only if magnetic_field_periodic=1
        period_length=0.1,  # syned Wiggler pars: used only if magnetic_field_periodic=1
        number_of_periods=10,  # syned Wiggler pars: used only if magnetic_field_periodic=1
        emin=100.0,  # Photon energy scan from energy (in eV)
        emax=200000.0,  # Photon energy scan to energy (in eV)
        # emin=2000.0,  # Photon energy scan from energy (in eV)
        # emax=2000.0,  # Photon energy scan to energy (in eV)
        ng_e=101,  # Photon energy scan number of points
        ng_j=501,  # Number of points in electron trajectory (per period) for internal calculation only
        flag_emittance=1,  # Use emittance (0=No, 1=Yes)
        shift_x_flag=4,  # 0="No shift", 1="Half excursion", 2="Minimum", 3="Maximum", 4="Value at zero", 5="User value"
        shift_x_value=0.001,  # used only if shift_x_flag=5
        shift_betax_flag=4,  # 0="No shift", 1="Half excursion", 2="Minimum", 3="Maximum", 4="Value at zero", 5="User value"
        shift_betax_value=0.0,  # used only if shift_betax_flag=5
    )

    # light source
    from shadow4.sources.wiggler.s4_wiggler_light_source import S4WigglerLightSource

    light_source = S4WigglerLightSource(name='wiggler', electron_beam=electron_beam, magnetic_structure=source, nrays=10000,
                                        seed=5676561)



    if False:
        traj, parms = light_source.get_trajectory()
        print(traj.shape, parms)
        from srxraylib.plot.gol import plot
        plot(traj[1, :], traj[0, :], xtitle="Y", ytitle="X")
        plot(traj[1, :], traj[3, :], xtitle="Y", ytitle="BetaX")
        plot(traj[1, :], traj[6, :], xtitle="Y", ytitle="Curvature")
        plot(traj[1, :], traj[7, :], xtitle="Y", ytitle="B")


        photon_energy, flux, spectral_power = light_source.calculate_spectrum()
        plot(photon_energy, flux, xtitle="photon energy [eV]", ytitle="Flux photons/s/0.001bw")


    beam = light_source.get_beam()
    # test plot
    from srxraylib.plot.gol import plot_scatter
    rays = beam.get_rays()
    plot_scatter(1e6 * rays[:, 0], 1e6 * rays[:, 2], title='(X,Z) in microns',   xrange=[-1800,100], yrange=[-100,100], show=0)
    plot_scatter(1e6 * rays[:, 3], 1e6 * rays[:, 5], title='(Xp,Zp) in microns', xrange=[-10000,8000], yrange=[-300,300])

