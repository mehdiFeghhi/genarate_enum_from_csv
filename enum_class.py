from enum import Enum
class hypercholesterolaemia(Enum):
   No = 0
   Yes = 1
   Missed = ?
class education(Enum):
   unread = 0
   sub_diploma = 1
   diploma = 2
   upon_diploma = 3
   Bachelor = 4
   MA = 5
   P.H.D = 6
class countryCode(Enum):
   Iran = 1
   other_country = 2
class marriageStatus(Enum):
   single = 0
   married = 1
   divorced = 2
   widow = 3
class gender(Enum):
   male = 0
   female = 1
class anginaCcs(Enum):
   Miseed = 0
   CCS0 = ?
   CCS1 = 1
   CCS2 = 2
   CCS3 = 3
   CCS4 = 4
class dyspnoea(Enum):
   Missed = 0
   NYHA_I = 1
   NYHA_II = 2
   NYHA_III = 3
   NYHA_IV = 4
   NAYHA_I = ?
   NAYHA_II = ?
   NAYHA_III = ?
   NAYHA_IV = ?
class numbarOfPreviousMyocardial(Enum):
   Missed = ?
   None = 0
   One = 1
   Two_or_more = 2
   Not_Known = 3
class mostRecentMyocardialInfarction(Enum):
   Missed = ?
   No_MI = ?
   MI_1_7_days_before_operation = ?
   MI<6_hours_before_operation = ?
   MI_6_24_hours_before_operation = ?
   MI_8_21_days_before_operation = ?
   MI_22_90_days_before_operation = ?
   MI_<_30_days_before_operation = ?
   90_>_MI_>_30_days_befor_operation = ?
   MI>90_days_before_operation = ?
class congestiveHeartFailure(Enum):
   Missed = ?
   No = 0
   Yes = 1
class previousPci(Enum):
   No_PCI = 0
   Not_Known = 1
   PCI<24_hours = 2
   PCI>_24_hours = 3
class addiction(Enum):
   Missed = ?
   Not_Known = ?
   No = 0
   Yes = 1
class diabetesTreatment(Enum):
   Missed = 0
   None = 1
   Diet = 2
   Oral_alone = 3
   Insulin = 4
   Insulin_(with_or_without_oral) = ?
class hypertension(Enum):
   No_hypertension = ?
   Treated_or_BP_>140/90_on_>1_occasions_prior_to_admission = ?
   Not_treated = ?
   Not_Known = ?
class choromicLungDisease(Enum):
   Missed = 0
   No = 1
   COPD = 2
   Asthema = 3
   COPD_/_Emphysema = ?
class numberOfDiseasedCoronaryVessels(Enum):
   no_vessel = ?
   one_vessel = ?
   two_vessel = ?
   three_vessel = ?
   not_investigation = ?
   Missed = ?
   No_vessel_with>50%_diameter_stenosis = ?
   One_vessel_with>50%_diameter_stenosis = ?
   Two_vessel_with>50%_diameter_stenosis = ?
   Three_vessel_with>50%_diameter_stenosis = ?
   Not_Investigation = ?
class leftMainStemDisease(Enum):
   Missed = ?
   No_LMS = 0
   LMS = 1
   Not_Investigation = 2
class ejectionFractionCategory(Enum):
   good = 1
   fair = 2
   poor = 3
   Not_measured = 4
class meanPawpLa(Enum):
   ? = ?
class ivNitratesHeparinOfAnyKind(Enum):
   Missed = 0
   No = 1
   Yes = 2
class ivIntropes(Enum):
   Missed = 0
   No = 1
   Yes = 2
class ventilated(Enum):
   Missed = 0
   No = 1
   Yes = 2
class cardiogenicShok(Enum):
   Missed = 0
   No = 1
   Yes = 2
class labp(Enum):
   No = 0
   Yes = 1
class exerciseToleranceTestETT(Enum):
   (+Ve) = 1
   (_Ve) = 2
   Not_Done = 3
   Missed = 4
class operativeUrgency(Enum):
   Elective = 1
   Urgent = 2
   Emergency = 3
   salvage = 4
class intraArorticPallonPump(Enum):
   No = 0
   Yes = 1
class Type of operation(Enum):
   on_pump = 0
   off_pump = 1
class otherCardiac(Enum):
   Missed = ?
   No = 0
   Yes = 1
class otherNonCardiac(Enum):
   Missed = ?
   No = 0
   Yes = 1
class poorMobility(Enum):
   No = 0
   Yes = 1
class criticalPreoperativeState(Enum):
   No = 0
   Yes = 1
class surgeryOnThoracicAorta(Enum):
   No = 0
   Yes = 1
class pulmonaryHypertension(Enum):
   ? = ?
class activeEndocarditis(Enum):
   No = 0
   Yes = 1
class stenosis_aorticValve(Enum):
   Missed = ?
   No = 0
   Yes = 1
class stenosis_miteralValve(Enum):
   Missed = ?
   No = 0
   Yes = 1
class stenosis_pulmonaryValve(Enum):
   Missed = ?
   No = 0
   Yes = 1
class stenosis_tricuspidValve(Enum):
   Missed = ?
   No = 0
   Yes = 1
class sufficiency_aorticValve(Enum):
   Missed = ?
   None = 0
   trival = 2
   mild = 3
   Moderate = 4
   Severe = 5
class sufficiency_miteralValve(Enum):
   Missed = ?
   None = 0
   trival = 2
   mild = 3
   Moderate = 4
   Severe = 5
class sufficiency_pulmonaryValve(Enum):
   Missed = ?
   None = 0
   trival = 2
   mild = 3
   Moderate = 4
   Severe = 5
class sufficiency_tricuspidValve(Enum):
   Missed = ?
   None = 0
   trival = 2
   mild = 3
   Moderate = 4
   Severe = 5
