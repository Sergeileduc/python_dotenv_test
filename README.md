# python_dotenv_test


## Local test :

Create `.env` file and define varenv :
`ABC_KEY="1234xyz"`

Run the test with `pytest`

For youtube tests to pass :
Create `TOKEN` varenv as well with your Youtube API token.


## Use Github actions and secret varenv

Add `ABC_KEY` and `TOKEN` in Github/Settings/Secret

Configure a Github Action workflow with pytest :

```
- name: Test with pytest
      env: # Or as an environment variable
        ABC_KEY: ${{ secrets.ABC_KEY }}
        TOKEN: ${{ secrets.TOKEN }}
      run: |
        pip install pytest
        pytest
```