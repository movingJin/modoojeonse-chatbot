# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates')],
    hiddenimports=[
            'eventlet',
            'eventlet.hubs.epolls',
            'eventlet.hubs.kqueue',
            'eventlet.hubs.selects',
            'engineio.async_drivers.eventlet',
            'dns', 
            'dns.dnssec',
            'dns.e164',
            'dns.namedict',
            'dns.tsigkeyring',
            'dns.update',
            'dns.versioned',
            'dns.zone'
    ],
    hookspath=['./hooks'],
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
    a.datas,
    [],
    name='modoojeonse-chatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
