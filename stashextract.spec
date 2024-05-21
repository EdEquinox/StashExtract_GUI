# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['stashextract.py'],
    pathex=[],
    binaries=[],
    datas=[('stashextract_gui/assets', 'stashextract_gui/assets')],
    hiddenimports=['stashextract_gui', 'customkinter'],
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
    name='stashextract.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True 
)

