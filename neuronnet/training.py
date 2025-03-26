from .collective_learning import AdamOptimizer

def collective_training(models, X, y, epochs, learning_rate, batch_size=32, early_stopping=False, patience=5):
    optimizer = AdamOptimizer(learning_rate)
    previous_loss = float('inf')
    for epoch in range(epochs):
        if early_stopping and epoch > 0 and loss > previous_loss:
            print("Early stopping triggered after {} epochs".format(patience))
            break

        for model in models:
            for i in range(0, X.shape[0], batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                output, hidden_output = model.forward(X_batch)
                model.backward(X_batch, y_batch, output, hidden_output, learning_rate)
        
        if epoch % 100 == 0: 
            print(f"Epoch {epoch}/{epochs} completed")
