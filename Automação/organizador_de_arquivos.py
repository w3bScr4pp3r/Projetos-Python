import pyautogui as pa


pa.PAUSE = 1 #Faz uma pausa de 1s entre os comandos


senha = 'sua_senha'
usuario = 'seu_usuario'

pa.hotkey('ctrl','alt','t')

pa.write('sudo su')
pa.press('enter')

pa.write(senha)
pa.press('enter')

pa.write(f'cd /home/{usuario}/Downloads')
pa.press('enter')

pa.write('Iniciando organização...')

pa.write('mkdir videos && mkdir musicas && mkdir imagens && mkdir docs && mkdir docs/compactados && mkdir docs/word && mkdir docs/excel && mkdir docs/powerPoint && mkdir docs/pdf')
pa.press('enter')

pa.write('mv *.doc *.docx *.txt /docs/word')
pa.press('enter')

pa.write('mv *.xls *.csv *.xlsx /docs/excel')
pa.press('enter')

pa.write('mv *.ppt *.pptx /docs/powerPoint')
pa.press('enter')

pa.write('mv *.zip *.rar *.tar.gz *.tgz /docs/compactados')
pa.press('enter')

pa.write('mv *.pdf /docs/pdf')
pa.press('enter')

pa.write('mv *.mkv *.avi *.mp4 /videos')
pa.press('enter')

pa.write('mv *.jpg *.png /imagens')
pa.press('enter')

pa.write('mv *.mp3 *.m4a /musicas')
pa.press('enter')

pa.write('Organização concluída.')
