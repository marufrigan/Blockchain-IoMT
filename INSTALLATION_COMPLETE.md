# ✅ Scyther Installation Complete!

## What Was Installed

1. **Scyther Tool** - Cloned from GitHub and built successfully
   - Location: `/Users/maruffarhan/Desktop/Blockchain IoMT/scyther/`
   - Binary: `scyther/gui/Scyther/scyther-mac`

2. **Dependencies Installed:**
   - ✅ CMake (via Homebrew)
   - ✅ Build tools (flex, bison, gcc - already present)

## How to Use Scyther

### Command-Line Usage (Recommended)

```bash
cd "/Users/maruffarhan/Desktop/Blockchain IoMT"
./scyther/gui/Scyther/scyther-mac protocol.spdl
```

### Python Wrapper (Alternative)

```bash
cd "/Users/maruffarhan/Desktop/Blockchain IoMT"
python3 scyther/gui/scyther.py protocol.spdl
```

## Current Status

✅ **Protocol File**: `protocol.spdl` - **Syntax is correct!**

⚠️ **Security Claims**: All claims are currently **failing** (attacks found)

This is **expected** for a simple 2-message protocol. The protocol needs additional security measures (like more message exchanges, proper nonce verification, etc.) to pass all security claims.

## Next Steps

1. **To view attack traces**: Run Scyther with XML or dot output:
   ```bash
   ./scyther/gui/Scyther/scyther-mac protocol.spdl --xml-output > results.xml
   ```

2. **To use GUI** (optional): Install wxPython:
   ```bash
   pip3 install wxPython
   python3 scyther/gui/scyther-gui.py
   ```

3. **Improve the protocol**: Based on the attack traces, add more security measures to make all claims pass.

## Files Created

- ✅ `protocol.spdl` - Your IoMT authentication protocol
- ✅ `SCYTHER_README.md` - Usage guide
- ✅ `INSTALLATION_COMPLETE.md` - This file

## Verification Results

When you run Scyther, you'll see:
- Claims that **pass** = ✅ Secure
- Claims that **fail** = ⚠️ Attack found (needs fixing)

Your protocol currently shows attacks, which is normal for a basic 2-message protocol. You can use Scyther's attack traces to understand the vulnerabilities and improve the protocol design.
