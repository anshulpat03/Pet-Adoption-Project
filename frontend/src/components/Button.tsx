import React from 'react';

interface ButtonProps {
  label: string;
  onClick?: () => void;
  style?: React.CSSProperties;
}

const Button: React.FC<ButtonProps> = ({ label, onClick}) => {
  return (
    <button onClick={onClick} className="custom-button">
      {label}
    </button>
  );
};

export default Button;
