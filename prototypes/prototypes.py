import sys
import os

from django.conf import settings

BASE_DIR=os.path.dirname(__file__)

settings.configure(
	DEBUG=True,
	SECRET_KEY='ki==706e99f0ps9w5s*!kx%1^=5jq_k1c&4r@#e&ng9=xlm5_',
	ROOT_URLCONF='sitebuilder.urls',
	MIDDLEWARE_CLASSES=(),
	INSTALLED_APPS=(
		'django.contrib.staticfiles',
		'django.contrib.webdesign',
		'sitebuilder',
		'compressor',

		),
	STATIC_URL='/static/',
	SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR,'pages'),
	SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR,'_build'),
	STATIC_ROOT=os.path.join(BASE_DIR,'_build','static'),
	#STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage',
	STATICFILES_FINDERS=(
		'django.contrib.staticfiles.finders.FileSystemFinder',
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
		'compressor.finders.CompressorFinder',

		)

)

if __name__ =="__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)