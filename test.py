import streamlit as st
import numpy as np

st.title("Generated VoIP Signal")

#typical sampling rate for VoIP is 16 kHz
seconds_of_signal = 1
number_of_samples = seconds_of_signal * 1600

#time axis values
time_axis = np.linspace(0, seconds_of_signal, number_of_samples)

#envelope to add smooth natural changes
envelope = np.convolve(np.random.rand(number_of_samples), np.ones(50)/50, mode='same')

#creates pauses
envelope[envelope < 0.5] = 0

frequencies_and_noise = (
    0.6 * np.sin(2 * np.pi * 120 * time_axis) +
    0.3 * np.sin(2 * np.pi * 220 * time_axis) +
    0.2 * np.sin(2 * np.pi * 300 * time_axis) +
    0.1 * np.random.randn(number_of_samples)
)

generated_signal = frequencies_and_noise * envelope

st.line_chart(generated_signal)
