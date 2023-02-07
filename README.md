# Text-to-Speech-TTS-Synthesis-with-Tortoise-and-PyTorch
Description: The code given can generate speech in your voice, utilizing Tortoise TTS and PyTorch. By taking your clean voice sample for 1 hour, the code can then say anything in your voice. The first step is installing the latest version of Scipy, followed by cloning the Tortoise library from GitHub and installing required packages. Imports are made, including PyTorch and Tortoise, and an instance of the TextToSpeech class is created. The code then defines the text to be spoken, the desired quality level (preset), and prompts the user to upload WAV files for the custom voice. Finally, the code generates speech with the custom voice, saves it as a WAV file, and displays it as an audio file. Tortoise enables high-quality speech generation from text with custom voices, useful in voice assistants, education, and entertainment applications.

Benefits: With Tortoise, it is possible to generate high-quality speech from text with custom voices. This can be useful in various applications, such as voice assistants, educational tools, and entertainment.

Scope of Functionalities: Tortoise provides a high-level API for TTS synthesis that can be used to generate speech from text. It supports custom voices and quality presets.

Screenshots: 
# add rfif wav voice samples
![image](https://user-images.githubusercontent.com/55629425/217155375-634a2196-cfee-4979-a964-4d8e0728f250.png)
#what to be spoken must be entered here
![image](https://user-images.githubusercontent.com/55629425/217155557-aeb563ae-418f-4dff-aabb-5c07c28cbaa5.png)
#voice generated must be downloaded here
![image](https://user-images.githubusercontent.com/55629425/217155659-dbd163cd-00e0-4e75-8da3-e01cca0d7452.png)



Development Resources:

Tortoise: https://github.com/jnordberg/tortoise-tts
PyTorch: https://pytorch.org/
Transformers: https://huggingface.co/transformers/
Torchaudio: https://github.com/pytorch/audio
Scipy: https://scipy.org/
