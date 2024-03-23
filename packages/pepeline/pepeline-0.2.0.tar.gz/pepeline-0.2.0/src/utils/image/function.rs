use std::path::Path;
use ndarray::{Axis, IxDyn};
use numpy::{PyArray, PyReadonlyArrayDyn, ToPyArray};
use pyo3::{Py, pyfunction, PyResult, Python};
use crate::utils::image::convert::{array_gray2image, array_grayf32_to_image, array_rgb2image, array_rgbf32_to_image, gray_img_open, gray_img_openf32, rgb_img_open, rgb_img_openf32};
use crate::utils::image::decode::{jpg_gray_img_open, jpg_gray_img_openf32, jpg_rgb_img_open, jpg_rgb_img_openf32, psd_din32_decode, psd_din_decode, psd_gray32_decode, psd_gray_decode, psd_rgb32_decode, psd_rgb_decode};

#[pyfunction]
pub fn save(
    input: PyReadonlyArrayDyn<u8>,
    out_path:String)
{
    // Saves images to the selected path.

    let array = input.as_array().to_owned();
    let shape = array.shape();
    match shape.len() {
        2 => {
            let img = array_gray2image(array.clone(),&shape);
            img.save(Path::new(&out_path)).expect("Not Save");
        }
        3 => {
            match shape[2]{
                3=>{let img = array_rgb2image(array.clone(),&shape);
                    img.save(Path::new(&out_path)).expect("Not Save");}
                1=>{
                    let array = array.clone().remove_axis(Axis(2)).into_owned();
                    let img = array_gray2image(array,&shape);
                    img.save(Path::new(&out_path)).expect("Not Save");
                }
                _=>{panic!("color channel error")}
            }}

        _ => {panic!("The array must be 2D or 3D")}
    }

}
#[pyfunction]
pub fn save32(
    input: PyReadonlyArrayDyn<f32>,
    out_path:String)
{
    // Saves images to the selected path.

    let array = input.as_array().to_owned();
    let shape = array.shape();
    match shape.len() {
        2 => {
            let img = array_grayf32_to_image(array.clone(),&shape);
            img.save(Path::new(&out_path)).expect("Not Save");
        }
        3 => {
            match shape[2]{
                3=>{let img = array_rgbf32_to_image(array.clone(),&shape);
                    img.save(Path::new(&out_path)).expect("Not Save");}
                1=>{
                    let array = array.clone().remove_axis(Axis(2)).into_owned();
                    let img = array_grayf32_to_image(array.clone(),&shape);
                    img.save(Path::new(&out_path)).expect("Not Save");
                }
                _=>{panic!("color channel error")}
            }}

        _ => {panic!("The array must be 2D or 3D")}
    }

}
#[pyfunction]
pub fn read<'py>(path: String, mode: Option<u8>, py: Python) -> PyResult<Py<PyArray<u8, IxDyn>>> {
    // reads the image using one of the modes, currently 0-gray8 mode=>1 rgb8
    let path = Path::new(&path);
    let extension = path.extension().and_then(|ext| ext.to_str()).unwrap_or("error");

    let mode = mode.unwrap_or(2u8);
    let array = match extension {
        "jpg"|"jpeg"=>{match mode {
            0 => jpg_gray_img_open(Path::new(&path)).into_dyn(),
            _ => jpg_rgb_img_open(Path::new(&path)).into_dyn(),
        }

        }
        "psd"|"PSD"=>{match mode {
            0 => psd_gray_decode(Path::new(&path)).into_dyn(),
            1 => psd_rgb_decode(Path::new(&path)).into_dyn(),
            _ => psd_din_decode(Path::new(&path)),
        }
        }

        "error"=>panic!("no_file"),
        _=>{match mode {
            0 => gray_img_open(Path::new(&path)).into_dyn(),
            _ => rgb_img_open(Path::new(&path)).into_dyn(),
        }}


    };

    Ok(array.to_pyarray(py).into())
}
#[pyfunction]
pub fn read32<'py>(path: String, mode: Option<u8>, py: Python) -> PyResult<Py<PyArray<f32, IxDyn>>> {
    // reads the image using one of the modes, currently 0-gray8 mode=>1 rgb8
    let path = Path::new(&path);
    let extension = path.extension().and_then(|ext| ext.to_str()).unwrap_or("error");

    let mode = mode.unwrap_or(2u8);
    let array = match extension {
        "jpg"|"jpeg"=>{match mode {
            0 => jpg_gray_img_openf32(Path::new(&path)).into_dyn(),
            _ => jpg_rgb_img_openf32(Path::new(&path)).into_dyn(),
        }

        }
        "psd"|"PSD"=>{match mode {
            0 => psd_gray32_decode(Path::new(&path)).into_dyn(),
            1 => psd_rgb32_decode(Path::new(&path)).into_dyn(),
            _ => psd_din32_decode(Path::new(&path)),
        }
        }
        "error"=>panic!("no_file"),
        _=>{match mode {
            0 => gray_img_openf32(Path::new(&path)).into_dyn(),
            _ => rgb_img_openf32(Path::new(&path)).into_dyn(),
        }}


    };
    Ok(array.to_pyarray(py).into())
}
