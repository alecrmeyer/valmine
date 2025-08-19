'use client';

import { useState, ChangeEvent, JSX } from 'react';

interface FormValues {
  economyRating: number;
  headshot_percentage: number;
  headshots: number;
  damage: number;
}

type FormField = keyof FormValues;

export default function Home(): JSX.Element {
  const [values, setValues] = useState<FormValues>({
    economyRating: 0,
    headshot_percentage: 0,
    headshots: 0,
    damage: 0
  });

  const [errors, setErrors] = useState<Partial<FormValues>>({});
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);

  const handleInputChange = (field: FormField, value: string): void => {
    setValues(prev => ({
      ...prev,
      [field]: value
    }));

    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({
        ...prev,
        [field]: undefined
      }));
    }
  };



  const handleSubmit = (): void => {
    console.log('Form submitted:', values);
    setIsSubmitted(true);
    setTimeout(() => setIsSubmitted(false), 3000);
    fetchSmurfPrediction();
  };


  async function fetchSmurfPrediction() {
    try{
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          econ_rating: values.economyRating,
          headshot_percentage: values.headshot_percentage,
          headshots: values.headshots,
          damage: values.damage
        })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Prediction result:', data);
    }
    catch(error: any) {
      console.error('Error fetching prediction:', error);}
  }


  const handleClear = (): void => {
    setValues({
      economyRating: 0,
      headshot_percentage: 0,
      headshots: 0,
      damage: 0
    });
    setErrors({});
    setIsSubmitted(false);
  };

  const inputFields: Array<{
    key: FormField;
    label: string;
    type: string;
    placeholder: string;
  }> = [
    {
      key: 'economyRating',
      label: 'Econ Rating',
      type: 'number',
      placeholder: 'Enter the econ rating...'
    },
    {
      key: 'headshot_percentage',
      label: 'Headshot Percentage',
      type: 'number',
      placeholder: 'Enter the headshot percentage...'
    },
    {
      key: 'headshots',
      label: 'Number of Headshots',
      type: 'number',
      placeholder: 'Enter the number of headshots...'
    },
    {
      key: 'damage',
      label: 'Damage',
      type: 'number',
      placeholder: 'Enter the amount of damage...'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl md:text-6xl font-bold text-white mb-4">
            Smurf <span className="text-purple-400">Or Not</span>
          </h1>
          <p className="text-slate-300 text-lg">
            Fill out the information below to determine if a player is a smurf or not.
          </p>
        </header>

        <div className="max-w-2xl mx-auto">
          <div className="backdrop-blur-sm bg-white/10 border border-white/20 rounded-2xl p-8 shadow-2xl">
            {isSubmitted && (
              <div className="mb-6 p-4 bg-green-500/20 border border-green-400/30 rounded-xl text-green-300 text-center">
                ✅ Form submitted successfully!
              </div>
            )}

            <div className="space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                {inputFields.map(({ key, label, type, placeholder }) => (
                  <div key={key} className="space-y-2">
                    <label className="block text-sm font-medium text-white/90">
                      {label} <span className="text-red-400">*</span>
                    </label>
                    <input
                      type={type}
                      value={values[key]}
                      onChange={(e: ChangeEvent<HTMLInputElement>) => 
                        handleInputChange(key, e.target.value)
                      }
                      className={`w-full px-4 py-3 bg-white/10 border rounded-xl text-white placeholder-white/50 focus:ring-2 focus:border-transparent outline-none transition-all backdrop-blur-sm ${
                        errors[key] 
                          ? 'border-red-400 focus:ring-red-400' 
                          : 'border-white/30 focus:ring-purple-400'
                      }`}
                      placeholder={placeholder}
                    />
                    {errors[key] && (
                      <p className="text-red-400 text-sm">{errors[key]}</p>
                    )}
                  </div>
                ))}
              </div>

              <div className="flex gap-4 pt-6">
                <button
                  onClick={handleSubmit}
                  className="flex-1 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 transform hover:scale-105 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
                  disabled={isSubmitted}
                >
                  {isSubmitted ? 'Submitted!' : 'Submit Form'}
                </button>
                <button
                  onClick={handleClear}
                  className="bg-white/20 hover:bg-white/30 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 border border-white/30"
                >
                  Clear
                </button>
              </div>
            </div>
          </div>

          {/* Live Preview */}
          <div className="mt-8 backdrop-blur-sm bg-white/5 border border-white/10 rounded-2xl p-6">
            <h3 className="text-lg font-semibold text-white mb-4">Live Preview:</h3>
            <div className="grid md:grid-cols-2 gap-4 text-sm">
              {inputFields.map(({ key, label }) => (
                <div key={key} className="text-white/70">
                  <span className="text-purple-300">{label}:</span>{' '}
                  {values[key] || '(empty)'}
                </div>
              ))}
            </div>
          </div>
        </div>

        <footer className="text-center mt-16 text-white/50 text-sm">
          <p>Built with Next.js, TypeScript, and Tailwind CSS</p>
        </footer>
      </div>
    </div>
  );
}