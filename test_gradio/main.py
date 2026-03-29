import gradio as gr


def greet(name):
    return f"Hello  {name}"


iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()


def main():
    print("Hello from test-gradio!")


if __name__ == "__main__":
    main()
