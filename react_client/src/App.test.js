import { render, screen } from '@testing-library/react';
import HighScoreList from './HighScoreList';

test('renders learn react link', () => {
  render(<HighScoreList />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
