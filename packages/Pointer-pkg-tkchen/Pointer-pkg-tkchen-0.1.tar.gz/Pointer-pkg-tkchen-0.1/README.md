## Pointer Package ReadMe

### Main class

- pointer.Pointer(object)
> Create a new pointer to the given object.

- - Pointer.get()
>> Get the object the pointer points to.

- - Pointer.set(object)
>> Set the object the pointer points to.

- - Pointer.address()
>> Get the memory address of the pointer points to.

*You don't need to free the pointer, because method __ del __ will help you to free the pointer automatically.*

### Methods

- pointer.sizeof(Pointer)
> Return the size of the object pointed to by the pointer.