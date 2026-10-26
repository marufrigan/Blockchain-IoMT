# Scyther Protocol Verification - Usage Guide

## File Created
- `protocol.spdl` - SPDL (Security Protocol Description Language) file for formal verification

## Protocol Overview

**Protocol Name:** PQCMFA (Post-Quantum Mutual Authentication)

**Roles:**
- **Patient (P)**: Medical device or patient entity
- **Server (S)**: Authentication server

**Protocol Flow:**
1. P → S: `{ID, NonceP}`
2. S → P: `{NonceS, SessionKey}pk(P)`

**Security Claims Verified:**
- ✅ **Alive**: Ensures both parties are alive and participating
- ✅ **Weakagree**: Weak agreement on the session key
- ✅ **Niagree**: Non-injective agreement on the session key
- ✅ **Nisynch**: Non-injective synchronization

These claims prove resistance against **Man-in-the-Middle (MITM) attacks**.

## How to Use with Scyther

### Step 1: Install Scyther
Download Scyther from: https://people.cispa.io/cas.cremers/scyther/

### Step 2: Open the Protocol File
1. Launch Scyther
2. File → Open → Select `protocol.spdl`

### Step 3: Verify the Protocol
1. Click "Verify" or press F5
2. Scyther will analyze the protocol and check all security claims
3. Review the results:
   - ✅ **Green checkmarks** = Claim verified (secure)
   - ❌ **Red X** = Attack found (vulnerability exists)

### Step 4: Interpret Results

**If all claims pass:**
- Your protocol is secure against the specified attacks
- You can include this in your research paper as formal verification proof

**If any claim fails:**
- Scyther will show an attack trace
- Review the attack scenario and refine your protocol
- Update the SPDL file and re-verify

## Syntax Notes

If you encounter syntax errors in Scyther, you may need to adjust:

1. **Message Format**: Some versions prefer tuples
   - Current: `send_1(Patient, Server, ID, NonceP)`
   - Alternative: `send_1(Patient, Server, (ID, NonceP))`

2. **Encryption Syntax**: May vary by version
   - Current: `pk(Patient, NonceS, SessionKey)`
   - Alternative: `{NonceS, SessionKey}pk(Patient)`

3. **Protocol Name**: Hyphens might need to be underscores
   - Current: `PQCMFA`
   - Alternative: `PQC_MFA` or `PQCMFA`

## Expected Verification Results

For a properly designed authentication protocol, you should see:
- ✅ All **Alive** claims verified
- ✅ All **Weakagree** claims verified (with proper nonces)
- ✅ All **Niagree** claims verified
- ✅ All **Nisynch** claims verified

## For Your Research Paper

When writing your paper, you can state:

> "We formally verified our authentication protocol using the Scyther tool. All security claims (Alive, Weakagree, Niagree, Nisynch) were verified, proving resistance against Man-in-the-Middle attacks."

Include a screenshot of the Scyther verification results showing all green checkmarks.

## Troubleshooting

**Error: "Unknown function pk"**
- Add function definition: `function pk(Agent, Data): Data;` at the top

**Error: "Protocol not found"**
- Check protocol name matches exactly
- Ensure file extension is `.spdl`

**Claims not verifying:**
- Review protocol logic - may need additional messages or nonces
- Check that fresh values are properly used
- Ensure encryption keys are correctly associated
