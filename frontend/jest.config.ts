import type {Config} from 'jest';

const config: Config = {
  clearMocks: true,
  testEnvironment: "jsdom",
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts'
  ],
  transform: {
    "^.+\\.(js|jsx|ts|tsx)$": "ts-jest",
    "^.+\\.svg$": "<rootDir>/jest/svgTransform.cjs",
    "^.+\\.(css|scss|sass)": "<rootDir>/jest/cssTransform.cjs",
  },
  setupFilesAfterEnv: [
    '<rootDir>/jest/jest.setup.ts'
  ],
};

export default config;
