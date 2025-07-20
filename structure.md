### _Old_ Structure:

```
music_downloader/
├── music_downloader/
│   ├── __init__.py          
│   ├── config.py            
│   ├── downloader.py        
│   ├── file_manager.py      
│   ├── logger.py            
│   └── utils.py             
├── tests/
│   ├── __init__.py          
│   ├── test_downloader.py   
│   ├── test_file_manager.py 
│   └── test_utils.py        
├── logs/
│   └── downloader.log       
├── main.py                  
├── README.md                
└── requirements.txt
```
---

### _New_ Structure:
```
music-downloader/
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── downloader.py
├── ui/
│   ├── __init__.py
│   ├── app.py
│   └── widgets.py
├── utils/
│   ├── __init__.py
│   └── file_handler.py
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── structure.md
├── TODO
└── uv.lock
```