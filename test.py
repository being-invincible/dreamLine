import solara

@solara.component
def Page():
    solara.Markdown("# Hello World!")
    solara.Button("Test Button", on_click=lambda: print("Button clicked!"))