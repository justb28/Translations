from ppm import read_ppm_as_rows, write_ppm, read_pgm_as_rows, write_pgm


def encrypt_image(image, key):
    # Convert key characters to ASCII strings
    encryption = [str(ord(c)) for c in key]
    print(f"Key: '{key}'")
    print(f"Encryption values: {encryption}")
    
    encrypted_image = []
    key_index = 0  # Track which key character we're using
    
    for row in image:
        encrypted_row = []
        for pixel in row:
            r, g, b = pixel
            
            # Get current key's ASCII string
            current_key_ascii = encryption[key_index % len(encryption)]
            
            # Pad with zeros if ASCII string is too short, or cycle through digits
            r_offset = int(current_key_ascii[0]) if len(current_key_ascii) > 0 else 0
            g_offset = int(current_key_ascii[1]) if len(current_key_ascii) > 1 else int(current_key_ascii[0]) if len(current_key_ascii) > 0 else 0
            b_offset = int(current_key_ascii[2]) if len(current_key_ascii) > 2 else int(current_key_ascii[0]) if len(current_key_ascii) > 0 else 0
            
            # Apply encryption (with wrapping to prevent overflow)
            r = (r ^ r_offset ) %255
            g = (g ^ g_offset ) %255
            b = (b ^ b_offset )%255
            
            encryption[key_index % len(encryption)]="000"  # Remove used key character
            encrypted_row.append((r, g, b))
            
            # Move to next key character
            key_index += 1
            
        encrypted_image.append(encrypted_row)
    
    return encrypted_image

def encrypt_imageP2(image, key):
    # Convert key characters to ASCII strings
    encryption = [d for c in key for d in str(ord(c))]
    print(f"Key: '{key}'")
    print(f"Encryption values: {encryption}")
    
    encrypted_image = []
    key_index = 0  # Track which key character we're using
    
    for row in image:
        encrypted_row = []
        for pixel in row:
            
            # Get current key's ASCII string
            current_key_ascii = encryption[key_index % len(encryption)]
            
            # Pad with zeros if ASCII string is too short, or cycle through digits
            val = (pixel ^ int(current_key_ascii)) % 255
            
            encryption[key_index % len(encryption)]="0"  # Remove used key character
            encrypted_row.append(val)
            
            # Move to next key character
            key_index += 1
            
        encrypted_image.append(encrypted_row)
    
    return encrypted_image

width,height,max_val, image = read_ppm_as_rows('color.ppm')
w,h,m, img = read_pgm_as_rows('p2.ppm')
key=input("Enter encryption key: ")
encrypted_image = encrypt_image(image, key)
write_ppm('encrypted_color.ppm', encrypted_image, max_val)
write_pgm('encrypted_p2.pgm', encrypt_imageP2(img, key), m)

