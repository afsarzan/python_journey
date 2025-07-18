from pathlib import Path #

path = Path("ecommerce/__init__.py")

#add action name to below file like 
print(f"exist {path.exists()}")
print(f"is file {path.is_file()}")
print(f"is dir {path.is_dir()}")
print(f"name {path.name}")
print(f"stem {path.stem}")
print(f"suffix {path.suffix}")
print(f"parent {path.parent}")
print(f"absolute {path.absolute()}")
print(f"resolve {path.resolve()}")
print(f"parts {path.parts}")
print(f"anchor {path.anchor}")
print(f"drive {path.drive}")
print(f"relative to cwd {path.relative_to(Path.cwd())}")
print(f"with name {path.with_name('new_init.py')}")
print(f"with suffix {path.with_suffix('.txt')}")
print(f"joinpath {path.joinpath('subdir', 'file.txt')}")
print(f"parent joinpath {path.parent.joinpath('subdir', 'file.txt')}")
print(f"glob {list(path.glob('*.py'))}")
print(f"rglob {list(path.rglob('*.py'))}")
print(f"iterdir {list(path.iterdir())}")
#     point2 = Point(1, 2)
