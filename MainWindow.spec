# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['MainWindow.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas+=[("add.png","D:\\app\\PyRSS\\assets\\add.png",'DATA'),
("cancle.png","D:\\app\\PyRSS\\assets\\cancle.png",'DATA'),
("collect.png","D:\\app\\PyRSS\\assets\\collect.png",'DATA'),
("quit.png","D:\\app\\PyRSS\\assets\\quit.png",'DATA'),
("read.png","D:\\app\\PyRSS\\assets\\read.png",'DATA'),
("share.png","D:\\app\\PyRSS\\assets\\share.png",'DATA'),
]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PyRss',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='D:\\app\\PyRSS\\icon.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
