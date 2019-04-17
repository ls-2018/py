import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
tips = sns.load_dataset('tips')
print(tips.head())