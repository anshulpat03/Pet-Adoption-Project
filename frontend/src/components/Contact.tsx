type ContactProps = {
  isOpen: boolean;
  onClose: () => void;
};

const Contact: React.FC<ContactProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="popup-overlay">
      <div className="popup-content">
        <h2>Contact Us</h2>
        <p>Agency Name: Pet Adoption Agency</p>
        <p>Email: contact@petadopt.com</p>
        <p>Phone: (123) 456-7890</p>
        <button onClick={onClose} className="popup-close-button">Close</button>
      </div>
    </div>
  );
};

export default Contact;
