import torch
import torch.nn as nn
import torch.optim as optim


class SkipgramModel(nn.Module):
    """
    A Skip-gram model for Word2Vec implementation. This model predicts the context words 
    given a target word.

    Attributes
    ----------
    embeddings : torch.nn.Embedding
        The embedding layer of the model.
    linear : torch.nn.Linear
        The linear layer of the model.
    """
    def __init__(self, vocab_size, embedding_dim):
        if not isinstance(vocab_size, int) or vocab_size <= 0:
            raise ValueError("vocab_size must be a positive integer.")
        if not isinstance(embedding_dim, int) or embedding_dim <= 0:
            raise ValueError("embedding_dim must be a positive integer.")
        
        super(SkipgramModel, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_size)
        
    def forward(self, context_word):
        emb = self.embeddings(context_word)
        out = self.linear(emb)
        return out

def train_model(model, idx_pairs, epochs=250, learning_rate=0.025):
    """
    Train the SkipgramModel.

    Parameters
    ----------
    model : SkipgramModel
        The model to train.
    idx_pairs : list of tuples
        The index pairs (context word, target word).
    epochs : int, optional
        The number of epochs to train for (default is 250).
    learning_rate : float, optional
        The learning rate for the optimizer (default is 0.025).
    """
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        total_loss = 0
        for context, target in idx_pairs:
            context_var = torch.tensor([context], dtype=torch.long)
            target_var = torch.tensor([target], dtype=torch.long)
            
            model.zero_grad()
            outputs = model(context_var)
            loss = criterion(outputs, target_var)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if (epoch+1)%10 ==0 or epoch == 0:
            print(f'Epoch: {epoch+1}, Loss: {total_loss}')
