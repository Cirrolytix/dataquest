import numpy as np
import pandas as pd

import gender_guesser.detector as gender


class GenderGuesser():

	NAME_GENDER_LOOKUP = {}
	GENDER_RESULT_RENAME = {'male':'masculine','female':'feminine',\
						'mostly_female':'mostly_feminine','mostly_male':'mostly_masculine',\
						'andy':'androgynous','unknown':'unknown'}

	def __init__(self):
		annot_gender_df = pd.read_csv('../data/name_gender_annot_corrected.csv')
		name_gender_lookup = dict(zip(annot_gender_df['first_name'],annot_gender_df['gender_corrected']))
		self.NAME_GENDER_LOOKUP =  name_gender_lookup

	def guess_gender(self, name):
		"""
		Returns
		'feminine'
		'mostly_feminine'
		'androgynous'
		'mostly_masculine'
		'masculine'
		"""
		d = gender.Detector()
		# get only first name
		name = name.split(" ")[0].capitalize()
		try:
			# use gender manual annotation if available
			return self.NAME_GENDER_LOOKUP[name]
		except:
			if any(s in name for s in ['lyn','mae','may','beth','leen','Lyn','Mae','Beth','May']):
				return 'feminine'
			elif any(name.endswith(s) for s in ['ie','la','na','ou','ia','ah','lle','fe','ene','eth','ette','ess','nn']):
				return 'feminine'
			elif any(name.endswith(s) for s in ['lo','yo','io','us','on','boy','mon','ard', 'old','ert','ark']):
				return 'masculine'
			else:
				return self.GENDER_RESULT_RENAME[d.get_gender(name)]