# returnalyze-kpis
This Python library is designed for the dynamic generation of kpi values for use within dashboard and anaytics team. It facilitates the easy retrieval of KPIs by applying filters such as client identifiers, environment settings, and date ranges. This modular approach not only enhances the insight generation process but also ensures adaptability for future requirements.

## Features
Generate KPI values dynamically 
Reusable across different modules, including insight generation processes.
Supports extensive filtering capabilities (client, environment, dates, etc.).
Designed for easy expansion to accommodate future enhancements.



## Update Package

Create your own account in [pypi.org](https://pypi.org/) and save the token you will use it soon.
@qqzhang72 to add you in pypi collabaror. 

1. Increment Package Version
in setup.py
```
setup(
    name='kpisQueryGeneration',
    version='0.1.1',  # Updated version number
    packages=find_packages(),
    install_requires=[
        ...
    ],
)

```
2. Rebuild Package
Before uploading again, clear out your existing dist/ directory to prevent attempts to re-upload old versions:
```
rm -rf dist

```
    
Then, rebuild your package with the new version number:
```
python setup.py sdist bdist_wheel
```

3. Upload New Version
You need to install twine if you don't have it. Here it will ask you the token for pypl.
```
twine upload dist/*
```
4. Check released version
In [pypi package released page](https://pypi.org/manage/project/kpisquerygeneration/releases/) check wether the new version get uploaded.


## Install Pacakge In Other Repos
Using version 0.1.5 as example 

1. Append  `kpisQueryGeneration==0.1.5` in either setup.py file or requirement.txt file.

2. Run cmd below in your teminal to install the kpisQueryGeneration
```
pip install kpisQueryGeneration==0.1.5 
```
If you meet problem, like download the new version but newer functions in it not reflecetd, considering just manually pip install the pacakage, this should solve the problem. 
Go to the Pypi page, here using [0.1.5 version](https://pypi.org/project/kpisQueryGeneration/0.1.5/#files) as example, either download the .whl (wheel) file or the source archive (.tar.gz).

Before downloading new pacakge, unintall the pacakge first.
```
pip uninstall kpisQueryGeneration
```

Then you have the file downloaded, you can install it using pip. Navigate to the directory where you've downloaded the file and run:
```
pip install kpisQueryGeneration-0.1.5-py3-none-any.whl
```
or if it's a source distribution:
```
pip install kpisQueryGeneration-0.1.5.tar.gz
```

3. Import library into the file and use it.
   For instance in returnalyze repo, in `returnalyze/resources/graphql/resolvers/reports/return_summary/kpi_summary.py` we want to use generate_template function from query_templating.query_utils in kpisQueryGeneration pacakge.
```
# Importing a specific utility from the submodule
from kpis_query_generation.generate_templates_and_params import generate_kpi_summary_template as test_generate_kpi_summary_template, generate_kpi_summary_params as test_generate_kpi_summary_params

...
def fetch_kpi_data(...):
    # test here
    template = test_generate_kpi_summary_template(return_rate_type, kpi_fetch_template, raw_kpi_fetch_template)

```
