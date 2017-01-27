Default Text-to-Speech
======================

The default text-to-speech plugin for Eva.

Doesn't sound pretty, but it's configurable and privacy-conscious (no internet communication).

Utilizes the [parente/espeakbox](https://github.com/parente/espeakbox) Docker container.

## Installation

Can be easily installed through the Web UI by using [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins).

Alternatively, add `default_tts` to your `eva.conf` file in the `enabled_plugins` option list and restart Eva.

The default configuration assumes you have run Eva using the [docker-compose](https://github.com/edouardpoitras/eva#first-steps) method and that the parente/espeakbox container is running.

If that isn't the case, try using the [Google Text-to-Speech](https://github.com/edouardpoitras/eva-google-tts) plugin instead.

## Usage

Once properly installed, Eva will start adding audio data to every response. This can be used by the clients to playback an appropriate audio response from Eva.

#### Audio Data

The clients should expect data with the following structure:

    data {
        'output_text': <text response here>,
        'output_audio': {
            'content_type': 'audio/wav', 'audio/mpeg', etc,
            'audio': <raw audio data>
        }
    }

## Configuration

Default configuration options can be changed by adding a `default_tts.conf` file in your plugin configuration path (can be configured in `eva.conf`, but usually `~/eva/configs`).

To get an idea of what configuration options are available, you can take a look at the `default_tts.conf.spec` file in this repository, or use the [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins) plugin and view them at `/plugins/configuration/default_tts`.

Here is a breakdown of the available options:

    pitch
        Type: Integer
        Default: 50
        The pitch of the voice used to respond to query/commands.
    rate
        Type: Integer
        Default: 175
        The voice speed in words per minute.
    voice
        Type: String
        Default: 'en'
        The name of the espeak voice to use.
    encoding
        Type: String
        Default: 'mp3'
        The encoding to use for the responding audio data (mp3 or ogg).
    tts_host
        Type: String
        Default: 'localhost'
        The host that is serving the parente/espeakbox container.
        'localhost' will work if running Eva with the docker-compose command.
    tts_port
        Type: Integer
        Default: 8081
        The port used by the host to server the parente/espeakbox container.
        '8081' is used by the docker-compose.yml file.
