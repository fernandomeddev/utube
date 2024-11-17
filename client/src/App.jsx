import React, { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header";
import CustomTable from "./components/CustomTable";
import VideoPlayer from "./components/VideoPlayer";
import Section from "./components/Section";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { getUrls, addUrl, deleteUrl } from "./services/fetchApi";
import Footer from "./components/Footer";
import Modal from "./components/Modal"; // Importando o novo Modal

function App() {
  const [url, setUrl] = useState("");
  const [urls, setUrls] = useState([]);
  const [view, setView] = useState("add");
  const [selectedUrl, setSelectedUrl] = useState(null);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  useEffect(() => {
    const fetchUrls = async () => {
      try {
        const data = await getUrls();
        setUrls(data);
      } catch (error) {
        toast.error("Não foi possível obter as URLs. Por favor, tente novamente mais tarde.");
      }
    };

    fetchUrls();
  }, []);

  const handleAddUrl = async () => {
    if (url && isValidYoutubeUrl(url)) {
      try {
        const newUrl = await addUrl(url);
        setUrls([...urls, newUrl]);
        setUrl("");
        toast.success("URL adicionada com sucesso!");
      } catch (error) {
        toast.error("Erro ao adicionar URL.");
      }
    } else {
      toast.error("Por favor, insira uma URL válida do YouTube.");
    }
  };

  const handleDeleteUrl = async (id) => {
    try {
      await deleteUrl(id);
      setUrls(urls.filter(url => url.id !== id)); // Remove a URL deletada da lista
      toast.info("URL deletada com sucesso.");
    } catch (error) {
      toast.error("Erro ao deletar URL.");
    }
  };

  const handleCloseModal = () => {
    setModalIsOpen(false);
    setSelectedUrl(null);
  };

  const handleOpenModal = (url) => {
    setSelectedUrl(url);
    setModalIsOpen(true);
  };

  const isValidYoutubeUrl = (url) => {
    const regex = /^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$/;
    return regex.test(url);
  };

  return (
    <div className="App-container">
      <div className="app-header">
        <Header />
      </div>
      
      <div className="App">
        <ToastContainer />

        {view === "add" && (
          <Section title="UTUBE ">
            <div>
              <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Insira a URL do YouTube"
                style={{ width: "300px", marginRight: "10px" }}
              />
              <button onClick={handleAddUrl}>Adicionar URL</button>
            </div>
          </Section>
        )}
          <Section title="">
            <CustomTable
              urls={urls}
              onDeleteUrl={handleDeleteUrl}
              onSelectUrl={handleOpenModal} // Abre o modal com o vídeo selecionado
            />
          </Section>

        {/* Modal que contém o VideoPlayer */}
        <Modal
          isOpen={modalIsOpen}
          onClose={handleCloseModal} // Fecha o modal
        >
          {selectedUrl && (
            <VideoPlayer
              watch_url={selectedUrl.watch_url}
            />
          )}
        </Modal>
      </div>
      <div className="footer-container">
        <footer className="app-footer">
          <Footer />
        </footer>
      </div>
    </div>
  );
}

export default App;
