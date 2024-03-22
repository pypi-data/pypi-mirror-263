extern crate sha2;
extern crate image;
extern crate pyo3;

use pyo3::prelude::*;
use pyo3::exceptions::PyOSError;
use sha2::Digest;
use std::io::{Cursor, Read};
use image::io::Reader as ImageReader;

#[pyfunction]
fn get_image_hash(_py: Python, _image_data: &[u8]) -> PyResult<String> {
    // Prefixing variables with underscores to suppress unused variable warnings
    let mut _image_data_vec = Vec::new();
    _image_data_vec.extend_from_slice(_image_data);
    let mut image_cursor = Cursor::new(_image_data_vec.clone()); // Cloning to avoid moving

    // Hash the image data using SHA-256
    let mut hasher = sha2::Sha256::new();
    let _ = image_cursor.read_to_end(&mut _image_data_vec); // Read image data into _image_data_vec
    hasher.update(&_image_data_vec); // Use cloned image data for hashing
    let hash = hasher.finalize();

    // Convert hash to hex string
    let hash_string = format!("{:x?}", hash);

    Ok(hash_string)
}

#[pymodule]
fn rust_image_hash(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(get_image_hash))?;
    Ok(())
}
