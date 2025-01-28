use std::{thread, time::Duration};

use norma::{models::whisper, Transcriber};

pub const POLLING_SECONDS: f32 = 5f32;

fn main() {
    let model_definition = whisper::monolingual::Definition::new(
        whisper::monolingual::ModelType::MediumEn,
        norma::models::SelectedDevice::Metal,
    );

    println!("Starting...");
    // loop {
    // 1. Poll the audio stream
    // 2. If there is silence, then stop the stream and transcribe
    // 3. If there is no silence, then continue polling
    // loop {
    let (join_handle, transcriber_handle) =
        Transcriber::blocking_spawn(model_definition.clone()).unwrap();

    let mut stream = transcriber_handle
        .blocking_start(norma::input::Settings::default())
        .unwrap();

    thread::spawn(move || {
        while let Some(seg) = stream.blocking_recv() {
            println!("{}", seg);
        }
    });

    thread::sleep(Duration::from_secs_f32(POLLING_SECONDS));

    transcriber_handle.stop().unwrap();
    drop(transcriber_handle);

    join_handle.join().unwrap().unwrap();

    println!("Restarting...");
    // }
}
