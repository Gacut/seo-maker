# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

# Analysis step: Analyze dependencies and configure build options
a = Analysis(
    ['SEOMaker.py'],  # Main Python script
    pathex=[],  # Additional paths for imports (if needed)
    binaries=[],  # Include any additional binaries if necessary
    datas=[
        ('resources/icon.ico', 'resources'),  # Include the application icon
        ('resources/example_input.txt', 'resources'),  # Include the example input prompt file
        ('resources/paraphraser_prompt.txt', 'resources'),  # Include the paraphraser prompt file
        ('resources/text_gen_prompt.txt', 'resources'),  # Include the text generation prompt file
        ('utils', 'utils')  # Include the utils folder in the output
    ],
    hiddenimports=[],  # Specify any hidden imports
    hookspath=[],  # Custom PyInstaller hooks (if any)
    runtime_hooks=[],  # Runtime hooks to execute
    excludes=[],  # Exclude specific modules from the build
    win_no_prefer_redirects=False,  # Use default Windows DLL behavior
    win_private_assemblies=False,  # Use shared assemblies
    cipher=block_cipher,  # Cipher for bytecode encryption (if needed)
    noarchive=False,  # Allow archiving to pack dependencies into a single file
)

# Bundle Python code into a standalone executable
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Define the main executable with GUI options and custom settings
exe = EXE(
    pyz,  # Compiled Python code
    a.scripts,  # Entry-point scripts
    [],
    exclude_binaries=True,  # Exclude binaries to avoid unnecessary files
    name='SEOMaker.exe',  # Name of the resulting executable
    debug=False,  # Disable debug mode
    bootloader_ignore_signals=False,  # Handle signals during bootloader execution
    strip=False,  # Do not strip debug symbols
    upx=True,  # Compress with UPX
    console=False,  # Disable console window (use GUI mode)
    icon='resources/icon.ico',  # Path to the application icon
)

# Collect all files and dependencies into the output folder
coll = COLLECT(
    exe,  # Main executable
    a.binaries,  # Binary dependencies
    a.zipfiles,  # Additional zip files (if any)
    a.datas,  # Data files to include (e.g., utils, resources)
    strip=False,  # Do not strip debug symbols
    upx=True,  # Compress with UPX
    upx_exclude=[],  # Exclude specific files from UPX compression
    name='SEOMaker',  # Name of the output folder in `dist/`
)
