import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../components/App';

test('renders learn react link', () => {
  render(<App />);
  const pre = screen.getByText("django-react-docker-heroku-template");
  expect(pre).toBeInTheDocument();
});
