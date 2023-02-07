# Text-to-Speech-TTS-Synthesis-with-Tortoise-and-PyTorch
Description: The code given above uses Tortoise, a text-to-speech (TTS) synthesis library based on PyTorch, to generate speech from text. The code first installs the latest version of Scipy and clones the Tortoise library from GitHub. It then installs the required packages, including the Transformers library from HuggingFace. After that, the code imports the necessary packages, including PyTorch and Tortoise, and creates an instance of the TextToSpeech class. The code then defines the text that will be spoken and the quality level ("preset"). The user is then prompted to upload WAV files to be used as the custom voice. Finally, the code generates speech with the custom voice, saves it as a WAV file, and displays it as an audio file in the notebook.

Benefits: With Tortoise, it is possible to generate high-quality speech from text with custom voices. This can be useful in various applications, such as voice assistants, educational tools, and entertainment.

Scope of Functionalities: Tortoise provides a high-level API for TTS synthesis that can be used to generate speech from text. It supports custom voices and quality presets.

Screenshots: 
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
