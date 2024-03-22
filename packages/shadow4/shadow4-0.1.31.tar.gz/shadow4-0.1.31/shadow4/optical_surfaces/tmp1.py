from shadow4.beamline.s4_beamline import S4Beamline

beamline = S4Beamline()

# electron beam
from shadow4.sources.s4_electron_beam import S4ElectronBeam
electron_beam = S4ElectronBeam(energy_in_GeV=6,energy_spread=0.001,current=0.2)
electron_beam.set_sigmas_all(sigma_x=3.01836e-05,sigma_y=4.36821e-06,sigma_xp=3.63641e-06,sigma_yp=1.37498e-06)

# magnetic structure
from shadow4.sources.undulator.s4_undulator_gaussian import S4UndulatorGaussian
source = S4UndulatorGaussian(
    period_length     = 0.042,     # syned Undulator parameter (length in m)
    number_of_periods = 38.571, # syned Undulator parameter
    photon_energy     = 5000.0, # Photon energy (in eV)
    delta_e           = 2.0, # Photon energy width (in eV)
    ng_e              = 100, # Photon energy scan number of points
    flag_emittance    = 1, # when sampling rays: Use emittance (0=No, 1=Yes)
    flag_energy_spread = 0, # when sampling rays: Use e- energy spread (0=No, 1=Yes)
    harmonic_number    = 1, # harmonic number
    flag_autoset_flux_central_cone  = 0, # value to set the flux peak
    flux_central_cone  = 10000000000.0, # value to set the flux peak
    )


# light source
from shadow4.sources.undulator.s4_undulator_gaussian_light_source import S4UndulatorGaussianLightSource
light_source = S4UndulatorGaussianLightSource(name='GaussianUndulator', electron_beam=electron_beam, magnetic_structure=source,nrays=50000,seed=5676561)
beam = light_source.get_beam()

beamline.set_light_source(light_source)

# optical element number XX
from syned.beamline.shape import Rectangle
boundary_shape = Rectangle(x_left=-0.001, x_right=0.001, y_bottom=-0.001, y_top=0.001)

from shadow4.beamline.optical_elements.absorbers.s4_screen import S4Screen
optical_element = S4Screen(name='Generic Beam Screen/Slit/Stopper/Attenuator', boundary_shape=boundary_shape,
    i_abs=0, # 0=No, 1=prerefl file_abs, 2=xraylib, 3=dabax
    i_stop=0, thick=0, file_abs='<specify file name>', material='Au', density=19.3)

from syned.beamline.element_coordinates import ElementCoordinates
coordinates = ElementCoordinates(p=27.2, q=0, angle_radial=0, angle_azimuthal=0, angle_radial_out=3.14159)
from shadow4.beamline.optical_elements.absorbers.s4_screen import S4ScreenElement
beamline_element = S4ScreenElement(optical_element=optical_element, coordinates=coordinates, input_beam=beam)

beam, footprint = beamline_element.trace_beam()

beamline.append_beamline_element(beamline_element)

# optical element number XX
from shadow4.beamline.optical_elements.crystals.s4_plane_crystal import S4PlaneCrystal
optical_element = S4PlaneCrystal(name='Plane Crystal',
    boundary_shape=None, material='Si',
    miller_index_h=1, miller_index_k=1, miller_index_l=1,
    f_bragg_a=False, asymmetry_angle=0.0,
    is_thick=1, thickness=0.001,
    f_central=1, f_phot_cent=0, phot_cent=15000.0,
    file_refl='bragg.dat',
    f_ext=0,
    material_constants_library_flag=0, # 0=xraylib,1=dabax,2=preprocessor v1,3=preprocessor v2
    )
from syned.beamline.element_coordinates import ElementCoordinates
coordinates = ElementCoordinates(p=10.9, q=0, angle_radial=1.54985, angle_azimuthal=0, angle_radial_out=1.48353)
movements = None
from shadow4.beamline.optical_elements.crystals.s4_plane_crystal import S4PlaneCrystalElement
beamline_element = S4PlaneCrystalElement(optical_element=optical_element,coordinates=coordinates, movements=movements, input_beam=beam)

beam, mirr = beamline_element.trace_beam()

beamline.append_beamline_element(beamline_element)


# test plot
if True:
   from srxraylib.plot.gol import plot_scatter
   plot_scatter(beam.get_photon_energy_eV(nolost=1), beam.get_column(23, nolost=1), title='(Intensity,Photon Energy)', plot_histograms=0)
   plot_scatter(1e6 * beam.get_column(1, nolost=1), 1e6 * beam.get_column(3, nolost=1), title='(X,Z) in microns')

# # test plot
# if 0:
#    from srxraylib.plot.gol import plot_scatter
#    plot_scatter(beam.get_photon_energy_eV(nolost=1), beam.get_column(23, nolost=1), title='(Intensity,Photon Energy)', plot_histograms=0)
#    plot_scatter(1e6 * beam.get_column(1, nolost=1), 1e6 * beam.get_column(3, nolost=1), title='(X,Z) in microns')
#
print(beam.intensity())
