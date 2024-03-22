// >>>> </> STANDARD IMPORTS </>
// >>>> ********************************************************************************
// use std::error::Error;
use std::time::{Duration, Instant};
// >>>> ********************************************************************************

// >>>> </> EXTERNAL IMPORTS </>
// >>>> ********************************************************************************
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use svg2pdf;
// >>>> ********************************************************************************

// ________________________________________________________________________________
#[pyfunction]
fn convert_svg_to_pdf(input_filepath: String, output_filepath: String) -> PyResult<()> {
    // Start the timer
    let start: Instant = Instant::now();

    // ________________________________________________________________________________
    // Read the SVG file into a string
    let svg: String = std::fs::read_to_string(&input_filepath)
        .map_err(PyErr::new::<pyo3::exceptions::PyIOError, _>)?;

    // ________________________________________________________________________________
    // Convert the SVG string to a PDF Vec<u8>
    let pdf: Vec<u8> = svg2pdf::convert_str(&svg, svg2pdf::Options::default())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;

    // ________________________________________________________________________________
    // Write to a file
    std::fs::write(output_filepath, pdf).map_err(PyErr::new::<pyo3::exceptions::PyIOError, _>)?;

    // Stop the timer
    let duration: Duration = start.elapsed();
    println!("- FILEPATH: {:} \n- TIME: {:?}", &input_filepath, duration);

    Ok(())
}

// ________________________________________________________________________________
#[pyfunction]
fn convert_svg_string_to_pdf(svg_string: String) -> PyResult<Vec<u8>> {
    // Start the timer
    let start: Instant = Instant::now();

    // ________________________________________________________________________________
    // Convert the SVG string to a PDF Vec<u8>
    let pdf: Vec<u8> = svg2pdf::convert_str(&svg_string, svg2pdf::Options::default())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;

    // Stop the timer
    let duration: Duration = start.elapsed();

    println!("- SVG-to-PDF TIME: {:?}", duration);

    Ok(pdf)
}

// ________________________________________________________________________________
// --- Python module setup
#[pymodule]
fn svg_to_pdf(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert_svg_to_pdf, m)?)?;
    m.add_function(wrap_pyfunction!(convert_svg_string_to_pdf, m)?)?;
    Ok(())
}
