# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['musicboardextract.py'],
    pathex=[],
    binaries=[],
    datas=[('musicboardextract_gui/assets', 'assets')],
    hiddenimports=['musicboardextract_gui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='musicboardextract.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True 
)

