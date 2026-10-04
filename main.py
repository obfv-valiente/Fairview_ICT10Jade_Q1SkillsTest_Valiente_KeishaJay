from pyscript import document, display

def create_order(event):
    prod1 = document.getElementById("prod1")
    prod2 = document.getElementById("prod2")
    prod3 = document.getElementById("prod3")
    prod4 = document.getElementById("prod4")
    prod5 = document.getElementById("prod5")

    subtotal = (float(prod1.value) * prod1.checked + float (prod2.value) * prod2.checked + float (prod3.value) * prod3.checked + float (prod4.value) * prod4.checked + float (prod5.value) * prod5.checked )


    taxrate= 0.12
    tax = subtotal * taxrate
    total= subtotal + tax

    document.getElementById("output1").innerHtml=""

    display(f"Subtotal:{subtotal}.", target="output1", append=False)
    display(f"Tax:{tax}.",target="output1",append=True)
    display(f"Total:{total}.", target="output1", append=True)
    display("Thank you for your order", target="output1", append= True)