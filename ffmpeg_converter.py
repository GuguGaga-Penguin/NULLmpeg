import subprocess
import os

def convert_media(input_file, output_file):
    """
    Converts an input media file to an output media file using FFmpeg.
    
    :param input_file: Path to the source file (e.g., 'video.mkv')
    :param output_file: Path for the converted file (e.g., 'video.mp4')
    """
    # Check if the input file actually exists
    if not os.path.exists(input_file):
        print(error_message := f"Error: Input file '{input_file}' not found.")
        return False

    # Build the FFmpeg command
    # -y automatically overwrites the output file if it already exists
    command = [
        'ffmpeg',
        '-y', 
        '-i', input_file,
        output_file
    ]
    
    try:
        print(f"Starting conversion: {input_file} -> {output_file}")
        
        # Run the command and wait for it to complete
        # text=True and capture_output=True lets us grab the error logs if it fails
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        
        print("Conversion completed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print("An error occurred during conversion:")
        print(e.stderr) # Prints the actual FFmpeg error log
        return False

# Example Usage
if __name__ == "__main__":
    # Replace these with your actual file paths
    source_file = "input.mov"
    destination_file = "output.mp4"
    
    convert_media(source_file, destination_file)
