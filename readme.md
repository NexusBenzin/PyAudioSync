# 🎵 PyAudioSync

> A Python application for syncing audio playback across multiple devices with real-time equalization and advanced routing configuration.

---

## ✨ Planned Features

- **Multi-device playback** — Route audio to multiple output devices simultaneously
- **Synchronized playback** — Keep all devices in sync using low-latency audio backends (JACK / ASIO)
- **Graphic & parametric EQ** — Per-device equalizer with configurable bands
- **Audio routing matrix** — Flexible routing between inputs and outputs
- **Real-time DSP** — Low-latency audio processing powered by `numpy` and `scipy`
- **Device management** — Detect, configure, and manage all connected audio devices
- **Profiles & presets** — Save and load EQ and routing configurations
- **Cross-platform** — Windows, Linux, and macOS support planned

---

## 🖥️ Planned Tech Stack

| Component | Library / Tool |
|---|---|
| Audio I/O | `sounddevice` / `pyaudio` |
| DSP / EQ | `numpy`, `scipy.signal` |
| Low-latency sync | JACK (Linux), ASIO (Windows) |
| GUI | `Tkinter` |
| Config management | `json` / `toml` |

---

## 📋 Usage (Planned)

Once implemented, PyAudioSync will work roughly like this:

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the GUI
python main.py
```
## 🗺️ Roadmap

### Phase 1 — Core Audio Engine
- [ ] Enumerate and list all available audio devices
- [ ] Play audio to a single output device
- [ ] Play the same stream to multiple devices simultaneously
- [ ] Basic volume control per device

### Phase 2 — Sync & Routing
- [ ] Implement clock sync for multi-device playback
- [ ] JACK backend support (Linux)
- [ ] ASIO backend support (Windows)
- [ ] Audio routing matrix (many-to-many)

### Phase 3 — EQ & DSP
- [ ] Graphic EQ (10-band)
- [ ] Parametric EQ (per-device)
- [ ] Real-time filter preview
- [ ] Low-latency DSP pipeline

### Phase 4 — GUI & Polish
- [ ] Full GUI with device manager
- [ ] EQ visualizer (frequency response curve)
- [ ] Save/load configuration profiles
- [ ] Installer & packaging

---

