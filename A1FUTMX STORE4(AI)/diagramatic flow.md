1.)
Raw CSV value
      ↓
Is it missing?
   ↓       ↓
  YES      NO
   ↓       ↓
None    Can I convert it?
            ↓       ↓
           YES      NO
            ↓       ↓
         integer   invalid
2.)

CSV
 ↓
Read
 ↓
Validate
 ↓
Convert types
 ↓
Handle missing data
 ↓
Handle invalid data
 ↓
Store valid values
 ↓
Calculate statistics



                 AI ENGINEER
                     │
       ┌─────────────┼─────────────┐
       │             │             │
      ML             DL          GenAI
       │             │             │
Statistics       Neural Nets      LLMs
       │             │             │
NumPy/Pandas     PyTorch         Transformers
       │             │             │
       └─────────────┼─────────────┘
                     │
              AI Engineering
                     │
          ┌──────────┴──────────┐
          │                     │
       Backend               Frontend
       Django                 React
       DRF                    TypeScript
          │                     │
          └──────────┬──────────┘
                     │
              Production AI
                     │
        APIs / Docker / Cloud
        Monitoring / Security
        Evaluation / Scaling
        