# Python Data Viewer Application

## Overview

The **Data Viewer** is a Qt Python application to view, edit, plot,
and filter data from various file types.  

The Data Viewer utilizes the `pandas` module along with the 
`Qt for Python` module to provide a familiar spreadsheet-like GUI for
any type of data that can be stored in a pandas `DataFrame`.  

The intention of this application is to provide a high-performance,
cross-platform application to review and analyze data. The Data
Viewer provides a faster and more optimized alternative for viewing and
plotting data files in a table format as opposed to other
applications such as Microsoft Excel or OpenOffice.

### Supported Input Formats

> Note: Input formats are automatically recognized based on the filename.  

The Data Viewer currently supports the following input formats:  

-   CSV (comma-delimited, tab-delimited)  

-   TXT (plain-text files)  

-   JSON (Javascript Object Notation)  

-   PICKLE (Python Pickle Format)  

-   XLSX (Microsoft Excel or OpenOffice files)  

### Supported Operating Systems

The following operating systems have been tested and confirmed to operate
the application nominally:  

-   Windows 10
-   MacOS Version 11.2 (Big Sur) using Apple M1
-   Linux (CentOS, Ubuntu)

Other operating systems are untested but will likely function if they are
supported by the Qt for Python version documented in requirements.txt

## Setup Instructions

### Dependencies

The following dependencies are required to run the data viewer application.

> Note: See [requirements.txt](requirements.txt) for the full dependency list including module versions.

-   `Python` (Version 3.6 or greater)
-   `pandas`
-   `numpy`  
-   `PyQt5`  
-   `openpyxl`  
-   `matplotlib`  
-   `QDarkStyle`  

### Application Setup / Installation

The Data Viewer uses `pip` to manage it's dependencies and can be setup using the commands below from the base directory of this repository.

> **Note: If you are using an Anaconda installation, you can skip these setup steps and proceed directly to the the [Running the Application](#running-the-application) section.**

#### Using a Python Virtual Environment (Recommended setup method)

> Windows (Git Bash)

```bash
virtualenv venv
source venv/Scripts/activate
pip install dataframeviewer
```  

> MacOS / Linux

```bash
virtualenv venv
source venv/bin/activate
pip install dataframeviewer
```  

#### Installing locally

> Note: The commands below can be used in Linux, MacOS, or Windows (Powershell, Git Bash, Cygwin, or WSL)

```bash
pip install dataframeviewer
```  

## Running the Application

> Run as a module

```bash
python -m dataframeviewer
```

> Run with sample data

```bash
python -m dataframeviewer --example
```

> Run with input file(s)

```bash
python -m dataframeviewer -f file1.csv file2.csv ...
```

> Show full command line option list

```bash
python -m dataframeviewer --help
```

> If using Anaconda 3 on windows with Git Bash installed, you can use the [run.sh](run.sh) script.

```bash
./run.sh
```
