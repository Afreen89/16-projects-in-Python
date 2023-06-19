from pathlib import Path

# base = Path.home()

# guide = Path(base, "Paris", "Eiffel_Tower.txt")
# guide = Path(base, "Europe", "France", Path("Paris", "Eiffel_Tower.txt"))
# guide2 = guide.with_name("Notre_Dame.txt")
# print(base)
# print(guide)
# print(guide2)
# print(guide.parent.parent)

# guide = Path(Path.home(), 'OneDrive\Desktop\jobs')
# print(guide)
# for txt in Path(guide).glob('*.txt'):
#     print(txt)


# guide = Path(Path.home(), 'OneDrive\\Desktop\\jobs\\afreen_jobs')
# # print(guide)
# # for txt in Path(guide).glob('**/*.odt'):
# for txt in Path(guide).glob('*.odt'):
#     print(txt)

guide = Path('Europe', 'France', 'Paris', 'Eiffel_Tower.txt')
in_europe = guide.relative_to(Path('Europe'))
in_france = guide.relative_to(Path('Europe', 'France'))

print(in_europe)
print(in_france)