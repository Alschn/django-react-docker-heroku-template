import {render, screen} from '@testing-library/react';
import Home from "../pages/Home";

test('renders home page with project name', () => {
  render(<Home/>);
  const text = screen.getByText("django-react-docker-heroku-template");
  expect(text).toBeInTheDocument();
});
