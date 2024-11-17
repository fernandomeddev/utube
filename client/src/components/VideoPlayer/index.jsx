import React from "react";
import "./styles.css"; // Estilos atualizados com ícones
import { toast } from "react-toastify";

function VideoPlayer({
  watch_url,
}) {
  const handleCopyLink = () => {
    navigator.clipboard.writeText(watch_url);
    toast.success("Link copiado para a área de transferência!");
  };

  // const date = new Date(publish_date);
  // const formattedDate = date.toISOString().split('T')[0]; // '2024-10-13'
  return (
    <div className="video-player">
      <div className="video-wrapper">
        <iframe
          className="video-iframe"
          src={watch_url.replace("watch?v=", "embed/")}
          title="YouTube video player"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
      </div>

      <div className="video-details">
        <div className="video-info">
          {/*
            NOVA VERSÃO COM A API DO YOUTUBE 
          <span className="video-icon">
            <i className="fas fa-eye"><p>{views}</p></i>
          </span>
          <span className="video-icon">
            <i className="fas fa-calendar-alt"><p>{publish_date}</p></i>
          </span>
          <span className="video-icon">
            <i className="fas fa-user"><p>{author}</p></i>
          </span> */}
        </div>
      </div>

      <div className="video-actions">
        <button className="icon-button copy-btn" onClick={handleCopyLink}>
          <i className="fas fa-link"></i>
        </button>
      </div>
    </div>
  );
}

export default VideoPlayer;
