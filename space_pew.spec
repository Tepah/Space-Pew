# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['space_pew.py'],
             pathex=['C:\\Users\\Tepah\\Documents\\GitHub\\Space_Pew'],
             binaries=[],
             datas=[("C:\\Users\\Tepah\Documents\\GitHub\\Space_Pew\\images\\*","images"),
             ("C:\\Users\\Tepah\Documents\\GitHub\\Space_Pew\\fonts\\Modak.ttf","fonts")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='space_pew',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
