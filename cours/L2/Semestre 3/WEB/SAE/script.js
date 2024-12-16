// ============================
//  MODELE
// ============================

class Game {
    constructor() {
        this.board = [
            ['Rhinocéros', 'Rhinocéros', 'Rhinocéros', 'Rhinocéros', 'Rhinocéros'],
            [null, null, null, null, null], 
            [null, null, null, null, null], 
            [null, 'Rocher', 'Rocher', 'Rocher', null], 
            [null, null, null, null, null], 
            [null, null, null, null, null],
            ['Éléphant', 'Éléphant', 'Éléphant', 'Éléphant', 'Éléphant']
        ];
        this.currentPlayer = 'Éléphant';
        this.reserve = {
            'Éléphant': 5,
            'Rhinocéros': 5
        };
        this.lastMove = null;
    }

    // Méthode pour réinitialiser la partie
    resetGame() {
        this.board = [
            ['Rhinocéros', 'Rhinocéros', 'Rhinocéros', 'Rhinocéros', 'Rhinocéros'],
            [null, null, null, null, null], 
            [null, null, null, null, null], 
            [null, 'Rocher', 'Rocher', 'Rocher', null], 
            [null, null, null, null, null], 
            [null, null, null, null, null],
            ['Éléphant', 'Éléphant', 'Éléphant', 'Éléphant', 'Éléphant']
        ];
        this.currentPlayer = 'Éléphant';
        this.lastMove = null;
    }

    isEmpty(x, y) { 
        return this.board[x][y] === null;
    }  

    isValidMove(fromX, fromY, toX, toY) {
        if (this.board[fromX][fromY] !== this.currentPlayer) {
            return false;
        }
        if (toX < 0 || toX >= 7 || toY < 0 || toY >= 5) {
            return false;
        }
        if (this.board[toX][toY] !== null) {
            return false;
        }
    
        const dx = Math.abs(fromX - toX);
        const dy = Math.abs(fromY - toY);
        return (dx + dy === 1);
    }

    movePiece(fromX, fromY, toX, toY) {
        if (!this.isValidMove(fromX, fromY, toX, toY)) {
            return false; 
        }
        this.board[toX][toY] = this.board[fromX][fromY];
        this.board[fromX][fromY] = null;              
        this.currentPlayer = this.currentPlayer === 'Éléphant' ? 'Rhinocéros' : 'Éléphant';
        return true;
    }

    handleSquareClick(fromX, fromY, toX, toY) {
        if (this.board[fromX][fromY] !== this.currentPlayer) {
            throw new Error("Vous devez déplacer une de vos pièces !");
        }
    
        if (!this.isValidMove(fromX, fromY, toX, toY)) {
            throw new Error("Déplacement invalide !");
        }
    
        const moveSuccessful = this.movePiece(fromX, fromY, toX, toY);
    
        if (!moveSuccessful) {
            throw new Error("Erreur lors du déplacement !");
        }

        if (this.checkVictory()) {
            alert(`${this.currentPlayer} a gagné !`);
            this.resetGame(); 
        } else {
            this.switchPlayer(); 
        }
    }

    switchPlayer() {
        this.currentPlayer = this.currentPlayer === 'Éléphant' ? 'Rhinocéros' : 'Éléphant';
    }

    isValidPlacement(x, y) {
        return this.board[x][y] === null;
    }

    placePiece(x, y) {
        if (this.isValidPlacement(x, y)) {
            this.board[x][y] = this.currentPlayer;
            this.reserve[this.currentPlayer]--;
            this.lastMove = { x, y };
            this.switchPlayer();
        } else {
            throw new Error("Placement interdit ! Respectez les règles : extrémités sauf colonne centrale.");
        }
    }

    movePieceWithRock(fromX, fromY, toX, toY) {
        if (!this.isValidMove(fromX, fromY, toX, toY)) {
            return false;
        }
        if (this.board[toX][toY] === 'Rocher') {
            const dx = toX - fromX;
            const dy = toY - fromY;
            const rockX = toX + dx;
            const rockY = toY + dy;
    
            if (rockX < 0 || rockX >= 5 || rockY < 0 || rockY >= 5 || this.board[rockX][rockY] !== null) {
                return false; 
            }
            this.board[rockX][rockY] = 'Rocher';
        }
    
        this.board[toX][toY] = this.board[fromX][fromY];
        this.board[fromX][fromY] = null;
        return true;
    }

    checkVictory() {
        for (let i = 0; i < 5; i++) {
            if (this.board[0][i] === 'Rocher' || this.board[6][i] === 'Rocher') {
                return true;
            }
        }
        return false;
    }
}

// ============================
//  VUE
// ============================

class View {
    constructor(game) {
        this.game = game;
        this.boardElement = document.getElementById('game-board');
        if (!this.boardElement) {
            this.boardElement = document.createElement('div');
            this.boardElement.id = 'game-board';
            document.body.appendChild(this.boardElement);
        }
    }

    renderBoard() {
        this.boardElement.innerHTML = '';
        this.boardElement.style.display = 'flex';
        this.boardElement.style.flexDirection = 'column';
        this.boardElement.style.alignItems = 'center';
        this.boardElement.style.justifyContent = 'center';
        this.boardElement.style.height = '100vh';
    
        for (let i = 0; i < this.game.board.length; i++) {
            const row = document.createElement('div');
            row.style.display = 'flex'; 
    
            for (let j = 0; j < this.game.board[i].length; j++) {
                const square = document.createElement('div');
                square.classList.add('square');
                square.style.width = '118px';
                square.style.height = '118px';
                square.style.display = 'flex';
                square.style.alignItems = 'center';
                square.style.justifyContent = 'center';
                square.dataset.index = i * 5 + j; 
                const piece = this.game.board[i][j];
                if (piece) {
                    const pieceElement = document.createElement('img');
                    pieceElement.src = `ressources/${piece.toLowerCase()}.png`;
                    pieceElement.classList.add('piece');
                    pieceElement.style.transform = piece === 'Rhinocéros' ? 'rotate(180deg)' : '';
                    pieceElement.style.height = '105px';
                    pieceElement.style.margin = '1px';
                    square.appendChild(pieceElement);
                }
                row.appendChild(square);
            }
            this.boardElement.appendChild(row);
        }
        this.attachSquareClickEvents();
    }

    attachSquareClickEvents() {
        const squares = this.boardElement.querySelectorAll('.square');
        let selectedSquare = null;
    
        squares.forEach((square, index) => {
            square.addEventListener('click', () => {
                const x = Math.floor(index / 5); 
                const y = index % 5;           
    
                try {
                    if (selectedSquare) {
                        const [fromX, fromY] = selectedSquare;
                        this.game.handleSquareClick(fromX, fromY, x, y);
                        selectedSquare = null;
                        this.renderBoard();  
                    } else {
                        if (this.game.board[x][y] === this.game.currentPlayer) {
                            selectedSquare = [x, y];
                            this.highlightSquare(x, y);
                        } else {
                            throw new Error("Sélectionnez une de vos pièces !");
                        }
                    }
                } catch (error) {
                    alert(error.message);
                }
            });
        });
    }

    afficherPopup(x, y) {
        const popup = document.createElement('div');
        popup.classList.add('popup');
        popup.style.width = '30%';
        popup.style.height = '30%';
        popup.style.position = 'fixed';
        popup.style.top = '40%';
        popup.style.left = '35%';
        popup.style.fontSize = '20px';
        popup.style.backgroundColor = 'wheat';
        popup.style.border = '1px solid black';
        popup.style.borderRadius = '30px';
        popup.style.display = 'flex';
        popup.style.flexDirection = 'column';
        popup.style.alignItems = 'center';
        popup.style.justifyContent = 'center';
        popup.style.zIndex = '1000';

        const directionText = document.createElement('p');
        directionText.innerText = 'Choisissez une direction :';
        popup.appendChild(directionText);

        const directions = ['Haut', 'Bas', 'Gauche', 'Droite'];
        directions.forEach(direction => {
            const button = document.createElement('button');
            button.innerText = direction;
            button.style.margin = '10px';
            button.addEventListener('click', () => {
                this.rotatePiece(x, y, direction);
                document.body.removeChild(popup);
            });
            popup.appendChild(button);
        });
        document.body.appendChild(popup);
    }

    rotatePiece(x, y, direction) {
        const pieceElement = this.boardElement.querySelectorAll('.square')[x * 5 + y].querySelector('img');
        switch (direction) {
            case 'Haut':
                pieceElement.style.transform = 'rotate(0deg)';
                break;
            case 'Bas':
                pieceElement.style.transform = 'rotate(180deg)';
                break;
            case 'Gauche':
                pieceElement.style.transform = 'rotate(270deg)';
                break;
            case 'Droite':
                pieceElement.style.transform = 'rotate(90deg)';
                break;
        }
    }

    showErrorMessage(message) {
        const errorElement = document.getElementById('error-message') || document.createElement('div');
        if (!errorElement.id) {
            errorElement.id = 'error-message';
            errorElement.style.color = 'red';
            errorElement.style.textAlign = 'center';
            errorElement.style.marginTop = '10px';
            document.body.appendChild(errorElement);
        }
        errorElement.innerText = message;
        errorElement.style.display = 'block';
        setTimeout(() => {
            errorElement.style.display = 'none';
        }, 3000);
    }

    highlightSquare(x, y) {
        const squares = document.querySelectorAll('.square');
        squares.forEach(square => square.classList.remove('clCliquable'));
        squares[x * 5 + y].classList.add('clCliquable');
    }
}

// ============================
//  CONTROLEUR
// ============================

class Controller {
    constructor(game, view) {
        this.game = game;
        this.view = view;
        this.initEvents();
        this.view.renderBoard();
    }

    initEvents() {
        document.getElementById('reset-btn').addEventListener('click', () => {
            this.game.resetGame();
            this.view.renderBoard();
        });
    }

    pushRock(fromX, fromY, toX, toY) {
        const directionX = toX - fromX;
        const directionY = toY - fromY;
        const nextX = toX + directionX;
        const nextY = toY + directionY;

        if (this.game.isEmpty(nextX, nextY)) {
            this.game.board[nextX][nextY] = 'Rocher';
            this.game.board[toX][toY] = this.game.currentPlayer;
            this.game.board[fromX][fromY] = null;
            this.game.lastMove = { x: toX, y: toY };
            this.game.switchPlayer();
        } else {
            throw new Error("Poussée interdite ! La case suivante n'est pas vide.");
        }
    }

    movePieceWithRock(fromX, fromY, toX, toY) {
        if (this.game.board[toX][toY] === 'Rocher') {
            this.pushRock(fromX, fromY, toX, toY);
        } else {
            this.game.movePiece(fromX, fromY, toX, toY);
        }
    }

    handleSquareClick(fromX, fromY, toX, toY) {
        if (this.game.isValidMove(fromX, fromY)) {
            this.movePieceWithRock(fromX, fromY, toX, toY);
        } else {
            throw new Error("Déplacement interdit ! Déplacez uniquement vos propres pièces.");
        }
    }
}

// ============================
//  INITIALISATION
// ============================

document.addEventListener('DOMContentLoaded', () => {
    const game = new Game();
    const view = new View(game);
    new Controller(game, view);
    view.renderBoard();
});
