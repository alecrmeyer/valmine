// next.config.js
module.exports = {
    async rewrites() {
        return [
          {
            source: '/predict',
            destination: 'http://127.0.0.1:8000/predict',
          },
        ]
      },
  };
