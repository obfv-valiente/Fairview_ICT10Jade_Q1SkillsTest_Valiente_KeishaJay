from pyscript import document, display

subtotal = (float(prod1.value) * prod1.checked + float (prod2.value) * prod2.checked + float (prod3.value) * prod3.checked + float (prod4.value) * prod4.checked + float (prod5.value) * prod5.checked )


display(f"Subtotal:{Subtotal}.", target="output1")
display(f"Tax:{tax}.",target="output1",append=True)
display(f"Total{total}.", target="output1", append=True)
display("Thank you for your order", target="output1", append= True)



            