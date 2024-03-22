// >>>> </> STANDARD IMPORTS </>
// >>>> ********************************************************************************
use std::error::Error;
use std::time::{Duration, Instant};
// >>>> ********************************************************************************

// >>>> </> EXTERNAL IMPORTS </>
// >>>> ********************************************************************************
use svg2pdf;
// >>>> ********************************************************************************

fn convert_svg_to_pdf(
    input_filepath: String,
    output_filepath: String,
) -> Result<(), Box<dyn Error>> {
    // ________________________________________________________________________________
    // --- Start the timer
    let start: Instant = Instant::now();

    // ________________________________________________________________________________
    // --- Read the SVG file into a string
    let svg: String = std::fs::read_to_string(&input_filepath)?;

    // --- Convert the SVG string to a PDF Vec<u8>
    // --- This can only fail if the SVG is malformed
    let pdf: Vec<u8> = svg2pdf::convert_str(&svg, svg2pdf::Options::default())?;

    // --- Now you have a Vec<u8> which you could write to a file or transmit over the network
    std::fs::write(output_filepath, pdf)?;

    // ________________________________________________________________________________
    // --- Stop the timer
    let duration: Duration = start.elapsed();

    println!("- FILEPATH: {:} \n- TIME: {:?}", &input_filepath, duration);

    // --- Return an Ok(()) to indicate success and that no value is being returned
    // --- This is the idiomatic way to indicate success in Rust
    return Ok(());
}

// >>>> ********************************************************************************
use std::thread;
// use std::sync::Arc;
// >>>> ********************************************************************************

fn main() {
    // - Start the timer
    let start: Instant = Instant::now();

    // - Define the input and output filepaths
    let input_filenames: Vec<String> = vec![
        "test0.svg".to_string(),
        "33.svg".to_string(),
        "test1.svg".to_string(),
        "test4.svg".to_string(),
        "test19.svg".to_string(),
        "test55.svg".to_string(),
    ];
    let mut handles = vec![];

    // - Convert each SVG file to PDF in a separate thread
    for input_filename in input_filenames {
        let input_filepath: String = format!("src/input_data/{}", &input_filename);
        let output_filepath: String =
            format!("src/output_data/{}", input_filename.replace(".svg", ".pdf"));

        let handle = thread::spawn(move || {
            // println!("CONVERTING FILE: {:?}", input_filename);
            // - If the conversion is successful, print a success message
            match convert_svg_to_pdf(input_filepath, output_filepath) {
                Ok(_) => println!("CONVERSION SUCCESSFUL\n---"),
                Err(e) => println!("Error for {}: {}", input_filename, e),
            }
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    // - Stop the timer
    let duration: Duration = start.elapsed();
    println!("--- TOTAL TIME: {:?}", duration);
}
