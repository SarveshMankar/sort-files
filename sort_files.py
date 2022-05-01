import os
import shutil
#Part 1, Getting all the Files
a=os.listdir('.')
b='.'
lst=[]
for i in a:
	if b in i:
		lst.append(i)
extensions=[]
for i in lst:
	b=i.split('.')
	extensions.append(str('.')+str(b[int(len(b))-1]).lower())

#Part 2, List of all the Extensions
Photos=['.png','.jpeg','.jpg','.tiff','.jfif','.ico']
Programming=['.css','.py','.java','.php','.html','.c','.cpp','.ipynb','.less','.asm' ,'.json','.joblib','.js','.asm','.xml','.xhtml','.kt',
			'kts','ktm','.swift']
Text=['.odt','.docx','.doc','.txt','.pdf','.wpd','.rtf','.ods','.odp','.ppt','.pptx','.url']
Music=['.mp3','.aac','.wav','.flac','.ram','.wma','.mpa','.ra']
Videos=['.mp4','.webm','.gif','.m4p','.mp2','.mov']
Data_Sets=['.csv','.db','.psql','.data','.xlsx','.sqlite','.accdb','.sql']
Compressed_and_Installer=['.zip','.deb','.rpm','.gz','.tar','.xz','.rar','.arj','.sit','.sitx','.7z','.exe','.msi','.ttf','.otf']
Torrent_Files=['.torrent']
Mobile_Apps=['.apk','.tpk','.ipa']
ISO_Files=['.iso']

#Part 3, Creating Required Folders
c=any(item in Photos for item in extensions)
if c:
	try:
		os.mkdir("Photos")
	except:
		pass

c=any(item in Programming for item in extensions)
if c:
	try:
		os.mkdir("Programming")
	except:
		pass

c=any(item in Text for item in extensions)
if c:
	try:
		os.mkdir("Text")
	except:
		pass

c=any(item in Music for item in extensions)
if c:
	try:
		os.mkdir("Music")
	except:
		pass

c=any(item in Videos for item in extensions)
if c:
	try:
		os.mkdir("Videos")
	except:
		pass

c=any(item in Data_Sets for item in extensions)
if c:
	try:
		os.mkdir("Data_Sets")
	except:
		pass

c=any(item in Compressed_and_Installer for item in extensions)
if c:
	try:
		os.mkdir("Compressed_and_Installer")
	except:
		pass

c=any(item in Torrent_Files for item in extensions)
if c:
	try:
		os.mkdir("Torrent_Files")
	except:
		pass

c=any(item in Mobile_Apps for item in extensions)
if c:
	try:
		os.mkdir("Mobile_Apps")
	except:
		pass

c=any(item in ISO_Files for item in extensions)
if c:
	try:
		os.mkdir("ISO_Files")
	except:
		pass

#Part 4, Sorting All the files
for i in lst:
	a=i.split('.')
	m=str('.')+str(a[len(a)-1])

	if m in Photos:
		try:
			shutil.move(str(i),"Photos")
		except:
			pass

	if m in Programming:
		try:
			shutil.move(str(i),"Programming")
		except:
			pass

	if m in Text:
		try:
			shutil.move(str(i),"Text")
		except:
			pass

	if m in Music:
		try:
			shutil.move(str(i),"Music")
		except:
			pass

	if m in Videos:
		try:
			shutil.move(str(i),"Videos")
		except:
			pass

	if m in Data_Sets:
		try:
			shutil.move(str(i),"Data_Sets")
		except:
			pass

	if m in Compressed_and_Installer:
		try:
			shutil.move(str(i),"Compressed_and_Installer")
		except:
			pass

	if m in Torrent_Files:
		try:
			shutil.move(str(i),"Torrent_Files")
		except:
			pass

	if m in Mobile_Apps:
		try:
			shutil.move(str(i),"Mobile_Apps")
		except:
			pass

	if m in ISO_Files:
		try:
			shutil.move(str(i),"ISO_Files")
		except:
			pass

print("Your Work is Done!")
a=input()
#Thanks