import React from "react";
import "./styles.css"; // O arquivo CSS para estilos

function CustomTable({ urls, onDeleteUrl, onSelectUrl }) {
  return (
    <table className="custom-table">
      <thead>
        <tr>
          <th>Título</th>
          <th>Autor</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {urls.length > 0 ? (
          urls.map((video) => (
            <tr
              key={video.id}
              onClick={() => onSelectUrl(video)}
              className="clickable-row"
            >
              <td data-label="Título">{video.title}</td>
              <td data-label="Autor">{video.author}</td>
              <td data-label="Ações">
                <button
                  className="delete-btn"
                  onClick={(e) => {
                    e.stopPropagation(); // Impede o clique de selecionar o vídeo ao clicar em "Excluir"
                    onDeleteUrl(video.id);
                  }}
                >
                  <span className="fas fa-trash"></span>
                </button>
              </td>
            </tr>
          ))
        ) : (
          <tr>
            <td colSpan="3">Nenhuma URL encontrada</td>
          </tr>
        )}
      </tbody>
    </table>
  );
}

export default CustomTable;
